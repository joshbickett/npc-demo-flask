# npc-demo-flask

This repository is a non-player character Flask API. It is setup and ready to go!

## setup instructions

First, clone the repo to your local computer

```
git clone https://github.com/joshbickett/npc-demo-flask.git
```

Change directory (CD) into the new folder.

```
cd npc-demo-flask-start
```

Create virtual envirnoment

```
python3 -m venv venv
```

Enter virtual environment

```
source venv/bin/activate
```

Then install the requirements for the project into your virtual environment

```
pip install -r requirements.txt
```

Then rename the `example.env` file to `.env` so that you can save your OpenAI key in it.

```
mv .env.example .env
```

Add your Open AI key to your new `.env` file so the app can use it.

```
OPENAI_API_KEY='your-key-here'
```

Deactivate and reactivate your virtual environment to load the env.

```
deactivate
source venv/bin/activate
```

Finally, you're ready, go ahead and start the app by running the following command.

```
flask run
```
