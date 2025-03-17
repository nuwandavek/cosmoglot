# cosmoglot
Intelligence vs languages: Are models dumb in some languages?


## goals
- Measure performance of a great model (gemma-3) in various languages from a well understood benchmark (gsm8k)
- Capture the activations at layer 16/17 from gemma-3; Train a sparse auto-encoder (SAE)
- Find features, clamp up/down and resurrect golden gate claude!

## problem setup: gsm8k
```
{
    'question': 'Mark has a garden with flowers. He planted plants of three different colors in it. Ten of them are yellow, and there are 80% more of those in purple. There are only 25% as many green flowers as there are yellow and purple flowers. How many flowers does Mark have in his garden?',
    
    'reasoning': "There are 80/100 * 10 = <<80/100*10=8>>8 more purple flowers than yellow flowers.\nSo in Mark's garden, there are 10 + 8 = <<10+8=18>>18 purple flowers.\nPurple and yellow flowers sum up to 10 + 18 = <<10+18=28>>28 flowers.\nThat means in Mark's garden there are 25/100 * 28 = <<25/100*28=7>>7 green flowers.\nSo in total Mark has 28 + 7 = <<28+7=35>>35 plants in his garden."

    'answer': 35
}
```

## findings
- I translated gsm8k to 5 languages
  - English (original)
  - French
  - Spanish
  - Hindi
  - Kannada
  - Sanskrit

- Ran the benchmark (5shot, like in the tech report) 

```
| question_language   |   correct |
|:--------------------|----------:|
| english             |      0.98 |
| french              |      0.93 |
| spanish             |      0.91 |
| hindi               |      0.91 |
| sanskrit            |      0.53 |
| kannada             |      0.51 |
```



- Got the activations ...
