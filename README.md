# NLP For Passion Web BackEnd

## Language, Framework and Plugins used :
- ### Python 3.6.9
- ### Flask micro-framework
- ### Heroku

## How to connect the Heroku NLPForPassion App?
- link API: https://nlpforpassion.herokuapp.com/


## Codes Dictionary:
|Codes | Describe |
| :--- |:--------|NLPForPassion
/

|1     | Success |
|0     | Error (Connection, Server doesn't active,... ) |
|100   | Wrong phone format |
|101   | Wrong password format |
|102   | Wrong password |
|103   | Account has not existed |
|104   | Phone has already existed |
|105   | No result

## Connect Dictionaries MongoDB Atlas Database:
- Connect by shell: 
```sh
mongo "mongodb+srv://cluster-iukdn.mongodb.net/<dbname>" --username firstData
```
- Connect by application: 
```sh
uri = "mongodb+srv://firstData:<password>@cluster-iukdn.mongodb.net/<dbname>?retryWrites=true&w=majority"
```
```sh
uri = "mongodb+srv://firstData:"+ password +"@cluster-iukdn.mongodb.net/<dbname>?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.dics
# collection: dics
```
- Connect by MongoDB Compass: 
```sh
mongodb+srv://firstData:<password>@cluster-iukdn.mongodb.net/test
```
```sh
<password>  = "firstdata10"
<dbname>    = "nlp"
<collection> = "dics"

## To Explore All Structures of function API:
- link: https://github.com/NLPForPassion/WebBackEnd/tree/master/APIsDesign

|Order | API Name | Completed | Describe |
| :--- |:---------|:---------|:---------|
| **###** | **###### USER #######** | **######** | **############################################** |
|1     | ChangePass | True | Change User Password but User have remembered his password |
|2     | LogIn | True | Log in into app by user account |
|3     | Register | True | Register into app for the first time exploring the app |
|4     | LogInByThirdParty | True | Log in into app by the third party (facebook, gmail, zalo,...) |
|5     | GetUserInfoByID | True | Get all of informations of one user account by ID |
|6     | UpdateInfoUser | True | Update all of informations of one user account |
| **###** | **###### HOUSING #####** | **######** | **############################################** |
|7     | PostHousing | True | Post one housing want to sell with some informations of that housing |
|8     | FindListHousing | True | Find all of housings depends on the features choosed by user want to find Housing |
|9     | GetListHousingIDsBySellerID | True | Get list housings IDs of one user account by his user ID |
|10     | DetailHousingByID | True | Get all of informations of one housing by its ID |
|11     | GetSomeInfoOfHousingArrayByIDs | True | Get some informations of housings (postID, address, postDay, square, price, content) have the ID in ID array |
|12     | GetDetailOfHousingArrayByIDs | True | Get all of informations of housings have the ID in ID array |
|13     | UpdateHousingInfo | False | Update some informations of Housing by its ID |
|14     | AddFavouriteHousing | True | Add one favourite housing include UserID & PostID|
|15     | GetListFavouriteHousingByUserID | True | Get List favourite Housing Posts by UserID |
|16     | UploadOneImage | False | Upload Only one image with binary array |
|17     | GetOneImageUrl | False | Get Only one Image with url Image |
|18     | UploadManyImage | False | Upload many images with binary arrays |
|19     | GetListImageUrls | False | Get Many Images with urls Image |
|20     | CompareListHousing | True | Show information compare of list housings |
