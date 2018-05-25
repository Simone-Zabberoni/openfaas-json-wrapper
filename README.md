# openfaas-json-wrapper
Simple skeleton openfaas wrapper in python for json input/output


1. Modify `entrypoint.py` as needed or uncomment one of the samples included in the script itself.
2. Test the modified script with your custom input or with mock json from https://jsonplaceholder.typicode.com/
3. Build the docker image
4. Deploy it in OpenFaas



## 1) Modify entrypoint

Uncomment the `"""` blocks to enable one sample function at time

## 2) Testing 

Usage example - extract only some fields:

```
$ cat mock.users.json | ./entrypoint.py
[
    {
        "username": "Bret",
        "name": "Leanne Graham"
    },
    {
        "username": "Antonette",
        "name": "Ervin Howell"
    },
[cut]
```

Usage example - DNS query and response:

```
$ cat mock.dnsquery.json
{
    "query": "facciocose.eu",
    "recordtype": "A"
}

$ cat mock.dnsquery.json | ./entrypoint.py 
{
    "status": "OK",
    "response_set": [
        {
            "response": "62.149.128.166"
        },
        {
            "response": "62.149.128.160"
        }
    ]
}
```

Usage example - Word and characters count

```
$ cat mock.text.json | ./entrypoint.py 
{
    "chars": "446",
    "rows": "1",
    "words": "69"
}
```

## 3) Build the image 

Add any needed dependancy in the Dockerfile, for instance to add a python library in the image uncomment:

```
COPY requirements.txt .
RUN pip install -r requirements.txt
```

Of course, you need to modify `requirements.txt` as well

Build and tag it accordingly:

```
docker build . -t sample-json-wordcount
Sending build context to Docker daemon  118.8kB
Step 1/10 : FROM python:3.4-alpine
3.4-alpine: Pulling from library/python
[cut]
```

You can run it on a non-standard port: 

```
$ docker run -p 6969:8080 sample-json-wordcount
2018/05/25 20:09:09 Writing lock-file to: /tmp/.lock
```

then double-check it with cURL:

```
$ curl -H "Content-Type: application/json" localhost:6969 -d "`cat mock.dnsquery.json`" 
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   600  100   545  100    55   2411    243 --:--:-- --:--:-- --:--:--  2411
{
    "response_set": [
        {
            "response": "62.149.128.163"
        },
        {
            "response": "62.149.128.157"
        },
[cut]
```

## 4) Deploy

Now you're ready to deploy the container as function, use openfaas-cli or the web UI


