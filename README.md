# HashIt
Hash your text with this tool (Works with API)
> API from **https://hashable.space/docs/api/usage**                   
> This tool needs **internet connection** to send request to API

# Install
+ clone
```bash
git clone https://github.com/MemeSec/HashIt && cd HashIt && chmod +x HashIt.py
```
+ requirements
```bash
pip install requests
```
+ usage
```bash
python HashIt.py
```

# Usage
To get result, you need to have three query parameters inside your request
```bash
Usage: HashIt.py --query=query --method=method --encode=encoding
Where:
  --query  : "your text"
  --method : md5 | sha256 | sha512
  --encode : hex | base64 | base64url

```

# Example
`python3 HashIt.py --query="12345" --encode=base64 --method=md5`        
![](https://readme-typing-svg.demolab.com?font=Fira+Code&size=15&pause=1000&color=F7F7F7&width=500&lines=WZRHGrsBESr8wYFZ9sx0tPURuZgG2lmzyvWpwXPKz8U%3D)

> Thanks <3
