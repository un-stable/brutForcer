import express from "express"
import bodyParser from "body-parser";

const app=express();
const port=8080;
app.use(bodyParser.urlencoded({ extended: true }))

app.post("/login",(req,res)=>{
    console.log(req.body);
    if(req.body.password=="booyaa"){
        res.send("great")
    }else{
        res.send("password incorrect.")
    }
   
   
})
app.get("/",(req,res)=>{
    res.send("server running ")
})

app.listen(port,()=>{
    console.log("server on port 8080")
})