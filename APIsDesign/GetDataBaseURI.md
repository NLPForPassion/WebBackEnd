# API: POST  
## Urlhttp:: https://nlpforpassion.herokuapp.com/getDataBaseURI
## REGEX 
## Request:
```sh  
    { 
        "name" : "DataBaseName"
    }
``` 
## Response: 
### Get success: 
```sh
    { 
        "error_code": 1,
        "data": { 
            "uri": "mongodb+srv://firstData:<password>@cluster-iukdn.mongodb.net/<dbname>?retryWrites=true&w=majority" 
        } 
    }
``` 
### Get fail: //chưa xong 
```sh
    { 
        "error_code": 100, 
        "error_message": "Wrong password format", 
        "data": null 
    }
    { 
        "error_code": 0, 
        "error_message": "Error", 
        "data": null 
    }
``` 