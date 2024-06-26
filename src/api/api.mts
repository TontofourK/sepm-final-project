import express from "express";
import { ResumeBot, createResumeBot } from "../modules/resumebot.mjs";
import { readFileSync } from "fs";
import cors from "cors";
import multer from "multer";
import { UnsafeCast } from "../util.js";
import { Model } from "../modules/bot.mjs"; 

const app = express();
const upload = multer();

const port = 8000;

let Output :string[] = []; 

app.use(cors());
app.use(express.json());

type File = Express.Multer.File; 

let LLM: ResumeBot; 

let output: string = "";

async function Main()
{
    LLM = await createResumeBot({
        Owner: "meta",
        Name: "meta-llama-3-70b-instruct"
    }, tokens => { output = LLM.Bot.Results[LLM.Bot.Results.length - 1].join(""); });  

    app.post("/upload", upload.array("resume"), async (req, res) => {
        await LLM.LoadResume(((UnsafeCast<File[]>(req.files))[0]).buffer.buffer);
        await LLM.Initialize();

        console.log("Reached here");

        await LLM.Tune(req.body.job_description);

        res.send({State: LLM.State});
    });

    app.get("/output", (req, res, id) => {
        const results: string[] = LLM.Bot.Results[LLM.Bot.Results.length - 1]; 

        res.send({ State: LLM.State, Output: (results !== undefined) ? results.join("") : ""});
    });

    app.listen(port, () => {
        console.log("Model:", LLM.Model);
        console.log(`Listening on port ${port}`);
    });
}

Main();