# Spiking and despiking
- checkout from master to a new branch created with a flag `-b`
```bash
git checkout -b passwordless-spike
```
- play around without writing tests - prototyping - a spike
- write some notes on a scratchpad
```
>    How to send emails
>    Generating and recognising unique tokens
>    How to authenticate someone in Django
>    What steps will the user have to go through?
```
- write a custom `User` model with only one single field - email
- write a model `Token` with email and uid field where uid the field gets a new uid number every time with 
`default=uuid.uuid4` (no braces)
- right before de-spiking we could write the first FT because it can help 
- revert the spiked code (switch back to master branch)
```bash
git checkout master
```
