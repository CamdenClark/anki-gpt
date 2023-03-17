# ChatGPT self-dialogue Anki card creation

Run the following:

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python anki.py
```

To edit the prompts, edit the `creator.md` and `critic.md`.

## Background

I find it frustrating to create Anki cards from information sometimes.

It was easy to get ChatGPT to create nicely formatted cards, but getting it to output reliably
the first time was very difficult. I often had to re-prompt the model with my feedback.

This is an experiment to see if starting with two different prompted characters, the creator and the critic,
can help to make ChatGPT more reliably output cards that are concise and easy to review.

I've subjectively found that doing it this way does help keep ChatGPT on track.

## TODOs

- Parse the front/back of the JSON
- Hook it up via API directly to AnkiConnect
- Allow up to 3 turns of feedback
- Support cloze deletions
- Package this up nicely with a CLI interface
