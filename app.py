from flask import Flask

app=Flask(__name__)
print("App initialized")

stores=[
    {
        "name":"my store",
        "items":[
            {
                "name":"Chair",
                "price" : 500.99
            }
        ]
    }
]

@app.get("/stores")
def get_stores():
    return {"stores" : stores}, 201
