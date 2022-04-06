### To run the project
1. create a virtaul environment with command virtaulenv <env:name> --python=python3.9
2. clone the project from github and open the project on vs code
3. in that run the command pip install -r requirements.txt
4. all the testing can be done on postman, A postman collection is also there in the project import it and start using it


## End points and there responses :

## 1. register user 

        endpoint-url : http://localhost:8000/register/

        headers : Content-Type application/json

        method : POST

        request :   {
                        "email": "",
                        "password": "",
                        "first_name": "",
                        "last_name": "",
                        "Phone": "",
                        "address": "",
                        "city": "",
                        "state": "",
                        "country": "",
                        "pincode": ""
                    }

        response : {
                        "email": "uniqueemail6@gmail.om",
                        "first_name": "shubham6",
                        "last_name": "jadhav6",
                        "Phone": "5555663588",
                        "address": "",
                        "city": "",
                        "state": "",
                        "country": "",
                        "pincode": "421301"
                    }


## 2. login user 

        endpoint-url : http://localhost:8000/login/

        headers : Content-Type application/json

        method : POST

        request :   {
                        "email":"uniqueemail5@gmail.om",
                        "password":"nokia300"
                    }

        response : {
                        "token": "057149ef210101d867d1b942b0b7838bb155cb99",
                        "id": 18
                    }

## 3. create category 

        endpoint-url : http://localhost:8000/category/

        headers : Content-Type application/json

        method : POST

        request :   {
                        "name":"category1"
                    }

        response : {
                        "name":"category1"
                    }

## 4. create content 

        endpoint-url : http://localhost:8000/content/

        headers : Content-Type application/json, 
                  Authorization: Token 8fa41ca7ca6553bc6630ef12014c04fc4ac7b485

        method : POST

        request = form data [{"key":"body","value":"this is a body2","type":"text","enabled":true},{"key":"summary","value":"this is a summary2","type":"text","enabled":true},{"key":"document","type":"file","enabled":true,"value":["/C:/Users/USER/Downloads/Python - Django Assignment.pdf"],"warning":"This file isn't in your working directory. Teammates you share this request with won't be able to use this file. To make collaboration easier you can setup your working directory in Settings."},{"key":"categories","value":"1","type":"text","enabled":true},{"key":"categories","value":"2","description":"","type":"text","enabled":true}]

        response : {
                        "title": "title2",
                        "body": "this is a body2",
                        "summary": "this is a summary2",
                        "document": "https://res.cloudinary.com/shub/image/upload/v1649226740/ymlsgjhymzve31h3kn7k.pdf",
                        "categories": [
                            5
                        ],
                        "author": 19
                    }

                    
## 5. author update content 

        endpoint-url : http://localhost:8000/update-content/<int:pk>/

        headers : Content-Type application/json, 
                  Authorization: Token 8fa41ca7ca6553bc6630ef12014c04fc4ac7b485

        method : PUT

        request = form data [{"key":"body","value":"this is a body2title2updated23","type":"text","enabled":true},{"key":"summary","value":"this is a summary2title2updated23","type":"text","enabled":true},{"key":"document","type":"file","enabled":true,"value":["/C:/Users/USER/Desktop/Learnings/lcomernbootcamp/tshirts/five.png"],"warning":"This file isn't in your working directory. Teammates you share this request with won't be able to use this file. To make collaboration easier you can setup your working directory in Settings."},{"key":"categories","value":"5","type":"text","enabled":true}]

        response : {
                        "title": "title2",
                        "body": "this is a body2",
                        "summary": "this is a summary2",
                        "document": "https://res.cloudinary.com/shub/image/upload/v1649226740/ymlsgjhymzve31h3kn7k.pdf",
                        "categories": [
                            5
                        ],
                        "author": 19
                    }
    
## 6. list content for loggedin user 

        endpoint-url : http://localhost:8000/list-content

        headers : Content-Type application/json, 
                  Authorization: Token 8fa41ca7ca6553bc6630ef12014c04fc4ac7b485

        method : GET

        response : [
                        {
                            "title": "title1",
                            "body": "this is a body",
                            "summary": "this is a summary",
                            "document": "https://res.cloudinary.com/shub/image/upload/v1649177096/jrjf3hoktev91d3zrepx.pdf",
                            "categories": [
                                1
                            ],
                            "author": 19
                        },
                        {
                            "title": "this is a title",
                            "body": "snfjsanfafklasnfasf",
                            "summary": "asfasfasfasf",
                            "document": "https://res.cloudinary.com/shub/image/upload/v1649180270/h5aoszenlcjy2qvslemu.pdf",
                            "categories": [
                                3,
                                4
                            ],
                            "author": 19
                        }
                    ]


## 7. admin content list 

        endpoint-url : http://localhost:8000/admin-list-content/

        headers : Content-Type application/json, 
                  Authorization: Token 8fa41ca7ca6553bc6630ef12014c04fc4ac7b485

        method : GET

        response : [
                        {
                            "title": "title1",
                            "body": "this is a body",
                            "summary": "this is a summary",
                            "document": "https://res.cloudinary.com/shub/image/upload/v1649177096/jrjf3hoktev91d3zrepx.pdf",
                            "categories": [
                                1
                            ],
                            "author": 19
                        },
                        {
                            "title": "title2",
                            "body": "this is a body2",
                            "summary": "this is a summary2",
                            "document": "https://res.cloudinary.com/shub/image/upload/v1649177151/wh10ti7rabvchax371u3.pdf",
                            "categories": [
                                1,
                                2
                            ],
                            "author": 18
                        },
                        {
                            "title": "this is a title",
                            "body": "snfjsanfafklasnfasf",
                            "summary": "asfasfasfasf",
                            "document": "https://res.cloudinary.com/shub/image/upload/v1649180270/h5aoszenlcjy2qvslemu.pdf",
                            "categories": [
                                3,
                                4
                            ],
                            "author": 19
                        }
                    ]

## 8. admin update content 

        endpoint-url : http://localhost:8000/admin-update-content/<int:pk>/

        headers : Content-Type application/json, 
                  Authorization: Token 8fa41ca7ca6553bc6630ef12014c04fc4ac7b485

        method : PUT

        request = form data [{"key":"body","value":"this is a body2title2updated23","type":"text","enabled":true},{"key":"summary","value":"this is a summary2title2updated23","type":"text","enabled":true},{"key":"document","type":"file","enabled":true,"value":["/C:/Users/USER/Desktop/Learnings/lcomernbootcamp/tshirts/five.png"],"warning":"This file isn't in your working directory. Teammates you share this request with won't be able to use this file. To make collaboration easier you can setup your working directory in Settings."},{"key":"categories","value":"5","type":"text","enabled":true}]

        response : {
                        "title": "title2",
                        "body": "this is a body2",
                        "summary": "this is a summary2",
                        "document": "https://res.cloudinary.com/shub/image/upload/v1649226740/ymlsgjhymzve31h3kn7k.pdf",
                        "categories": [
                            5
                        ],
                        "author": 19
                    }
    
## 9. admin delete content 

        endpoint-url : http://localhost:8000/admin-delete-content/<int:pk>/

        headers : Content-Type application/json, 
                  Authorization: Token 8fa41ca7ca6553bc6630ef12014c04fc4ac7b485

        method : DELETE

    
## 10. author delete content 

        endpoint-url : http://localhost:8000/delete-content/<int:pk>/

        headers : Content-Type application/json, 
                  Authorization: Token 8fa41ca7ca6553bc6630ef12014c04fc4ac7b485

        method : DELETE

## 11. search content by user

        endpoint-url : http://localhost:8000/question/?search=shubham

        headers : Content-Type application/json, 
                  
        method : GET

        response : [
                        {
                            "title": "title1",
                            "body": "this is a body",
                            "summary": "this is a summary",
                            "document": "https://res.cloudinary.com/shub/image/upload/v1649177096/jrjf3hoktev91d3zrepx.pdf",
                            "categories": [],
                            "author": 19
                        }
                    ]

    