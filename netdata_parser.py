import argparse,json
from pathlib import Path
def parse(path):
 rows=[]
 for n,line in enumerate(Path(path).read_text(encoding="utf-8",errors="replace").splitlines(),1):
  if not line.strip():continue
  try:rows.append(json.loads(line))
  except json.JSONDecodeError:rows.append({"_parse_error_line":n})
 return {"records":len(rows),"valid":sum("_parse_error_line" not in r for r in rows),"invalid":sum("_parse_error_line" in r for r in rows)}
def main():
 a=argparse.ArgumentParser();a.add_argument("file");x=a.parse_args();print(json.dumps(parse(x.file),indent=2))
if __name__=="__main__":main()
