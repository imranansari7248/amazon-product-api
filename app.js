import { spawn } from 'child_process';
import express from 'express';
import bodyParser from 'body-parser';
import path from 'path';
import { fileURLToPath } from 'url';
import ejs from 'ejs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));
app.set('view engine', 'ejs');


app.get('/', (req, res) => {
    res.redirect('/help')
})

app.get('/query', (req, res) => {
    if (req.query.query) {
        const pythonScript = spawn('python', ['./scrap_by_query_string.py', query], { shell : true});

        let results;
        pythonScript.stdout.on('data', data => {
            results = JSON.parse(data) 
        })
        
        pythonScript.on('close', code => {
            res.json(results)
        })
    }
    else {
        console.log('not query')
    }
})


app.get('/api', (req, res) => {
    if (Object.keys(req.query).length == 0) {
        res.json({
            status: 'api is live',
            message: `visit : http://localhost:3000/help for help`
        }) 
        return 
    } else {
        if (!req.query.query) {
            res.json({
                error: 'query parameter is missing',
                message: `visit : http://localhost:3000/help for help`
            })
            return
        }
        const query = req.query.query;
        const page = req.query.page ? req.query.page : '1';
        const price = req.query.price ? req.query.price : '0';
        const brand = req.query.brand ? req.query.brand : 'all';
        console.log(query, page , price, brand);
        const pythonScript = spawn('python', ['./scrapers/scrap_by_query_string.py', '-query' , query, '-price', price, '-brand', brand , '-page', page], { shell : true});
    
        let results;
        pythonScript.stdout.on('data', data => {
            results = JSON.parse(data) 
        })
        
        pythonScript.on('close', code => {
            res.json(results)
        })
    }
})

app.get('/link', (req, res) => {
    console.log(req.query)
    if (Object.keys(req.query).length == 0) {
        res.json({
            error: 'parameters is missing',
            message: `visit : http://localhost:3000/help for help`
        }) 
        return 
    } else {
        if (!req.query.link) {
            res.json({
                error : 'link parameter is missing',
                message: `visit : http://localhost:3000/help for help`
            })
        }
        const link = req.query.link;
        const pythonScript = spawn('python', ['./scrapers/scrap_by_link.py', link], { shell : true});

        let results;
        pythonScript.stdout.on('data', data => {
            results = JSON.parse(data) 
        })

        pythonScript.on('close', code => {
            res.json(results)
        })
    }
})

app.get('/help' , (req, res) => {
    res.render('index');
})

app.listen(process.env.PORT, () => {
    console.log('Server started on port 3000');
})


