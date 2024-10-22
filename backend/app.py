from flask import Flask, jsonify
import random, requests
app = Flask(__name__)

chuck_norris_facts = [
    "Chuck Norris threw a grenade and killed 50 people. Then it exploded.",
    "When Chuck Norris enters a room, he doesn't turn the lights on. He turns the dark off.",
    "Chuck Norris can hear sign language.",
    "Chuck Norris can do a wheelie on a unicycle.",
    "Once, a cobra bit Chuck Norris’ leg. After five days of excruciating pain, the cobra died.",
    "Chuck Norris counted to infinity. Twice.",
    "Chuck Norris can divide by zero.",
    "When Chuck Norris enters a room, he doesn’t turn the lights on. He turns the dark off.",
    "Chuck Norris can slam a revolving door.",
    "Chuck Norris once roundhouse kicked someone so hard that his foot broke the speed of light.",
    "Chuck Norris can unscramble an egg.",
    "Chuck Norris doesn’t read books. He stares them down until he gets the information he wants.",
    "Time waits for no man. Unless that man is Chuck Norris.",
    "If you spell Chuck Norris in Scrabble, you win. Forever.",
    "Chuck Norris breathes air ... five times a day.",
    "In the Beginning there was nothing ... then Chuck Norris roundhouse kicked nothing and told it to get a job.",
    "When God said, “Let there be light!” Chuck Norris said, “Say Please.”",
    "Chuck Norris has a mug of nails instead of coffee in the morning.",
    "If Chuck Norris were to travel to an alternate dimension in which there was another Chuck Norris and they both fought, they would both win.",
    "The dinosaurs looked at Chuck Norris the wrong way once. You know what happened to them.",
    "Chuck Norris' tears cure cancer. Too bad he has never cried.",
    "If you ask Chuck Norris what time it is, he always says, 'Two seconds till.' After you ask, 'Two seconds to what?' he roundhouse kicks you in the face.",
    "Chuck Norris appeared in the 'Street Fighter II' video game, but was removed by Beta Testers because every button caused him to do a roundhouse kick. When asked about this “glitch,” Chuck Norris replied, “That's no glitch.”",
    "Since 1940, the year Chuck Norris was born, roundhouse kick related deaths have increased 13,000 percent.",
    "Chuck Norris does not own a stove, oven or microwave, because revenge is a dish best served cold.",
    "Chuck Norris does not sleep. He waits.",
    "There is no chin behind Chuck Norris' beard. There is only another fist.",
    "The chief export of Chuck Norris is pain.",
    "Chuck Norris recently had the idea to sell his pee as a canned beverage. It’s now called Red Bull.",
    "If paper beats rock, rock beats scissors, and scissors beats paper, what beats all 3 at the same time? Chuck Norris.",
    "On the 7th day, God rested ... Chuck Norris took over.",
    "Chuck Norris can dribble a bowling ball.",
    "Chuck Norris drinks napalm to fight his heartburn.",
    "Chuck Norris' roundhouse kick is so powerful, it can be seen from outer space by the naked eye.",
    "If you want a list of Chuck Norris' enemies, just check the extinct species list.",
    "Chuck Norris has never blinked in his entire life. Never.",
    "Chuck Norris once shot an enemy plane down with his finger, by yelling, “Bang!”",
    "Chuck Norris does not use spell check. If he happens to misspell a word, Oxford will change the spelling.",
    "Some kids pee their name in the snow. Chuck Norris can pee his name into concrete.",
    "Chuck Norris can kill two stones with one bird.",
    "Chuck Norris mines bitcoin with a pickaxe.",
    "Chuck Norris’ trash throws itself out.",
    "When a building is on fire and Chuck Norris walks in, the Chuck Norris alarm rings.",
    "Chuck Norris used to wash his clothes in the ocean, but it caused too many tsunamis.",
    "Chuck Norris doesn’t go hunting because the “hunting” implies that you might not succeed. Chuck Norris goes killing.",
    "Chuck Norris can charge a cell phone by rubbing it against his beard.",
    "Chuck Norris once roundhouse kicked a man so hard that it was felt by his ancestors.",
    "Chuck Norris has counted to infinity twice.",
    "Chuck Norris can clap with only one hand.",
    "Chuck Norris used to beat up his shadow because it was constantly too close. Now it stands a safe 30 feet behind him."
]


@app.route('/fact', methods=['GET'])
def get_fact():
    return jsonify({"fact": random.choice(chuck_norris_facts)})

@app.route('/chuck', methods=['GET'])
def get_chuck():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    print(response.json())
    return jsonify({"quote": response.json()['value']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)