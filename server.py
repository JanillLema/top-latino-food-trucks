from flask import Flask
from flask import render_template, Response, request, jsonify, redirect, url_for
import json
app = Flask(__name__)

# food truck data
food_trucks = [
    {
    "id": 0,
    "state": "Texas",
    "name": "Veracruz All Natural",
    "img": "https://i.ibb.co/TP6QxnC/1.png",
    "about": "Family/Latina/Women run & inclusive to all, founded in Austin, TX. Currently, it can be found in FIVE Austin locations and costs less than your morning coffee to grab one of their famous tacos (they have both breakfast and lunch tacos).There's something for everyone: vegans, pescatarians, meat-lovers, or just really hungry lunch-goers.Don't forget about their delicious drink menu, including options like lime juice, cantaloupe, apple, grape, and pineapple smoothie!",
    "rating": 4.5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "This food truck is a) so cute b) SO TASTY. We came on a Saturday morning after spending way too long looking at lists of the best breakfast tacos in Austin and these clearly made the list for a reason. I got one La Reyna and one Migas Poblanas taco, and they were both GREAT. Their salsas definitely add a little kick too, so I'd add them. These were the best breakfast tacos I had during my trip!"},{ "mark_as_deleted" : False, "review" : "Veracruz was recommended by many of our friends so had to give it a try. We first tried to go to Franklin's bbq but the line was outrageous so we went to Veracruz. This was around 1:30 so figured the line wouldn't be too bad.. wrong. We were about 10th in line and a lot had sold out by that point. We ended up getting a Migas poblano, chicken mole and al pastor. The highlight for me were the salsas. They were absolutely divine. The hot salsa had a kick but soo flavorful and packed with heat. The corn tortillas on the tacos were delicious and filling as each had two tortillas per taco. I would definitely go again but if there was a lot sold out, It wouldn't be worth it."},{ "mark_as_deleted" : False, "review" : "If you are looking for great tacos for breakfast or lunch or dinner, look no further.We came for breakfast in a Saturday morning. The lines are loooong and sitting is on benches outside. First, you need to order the food, you give them your cell number and you are called when it's time to pick up the food.I had the poblanas and fish tacos. The fish was very tasty but a bit too salty.My daughter had tHe original for breakfast and I think it was a bit better than the poblanas. The chips and guacamole is very good too."}],
    "location":"1704 E Cesar Chavez Austin, TX 78702"
    },
    {
    "id": 1,
    "state": "Texas",
    "name": "Tacoholics",
    "img": "https://i.ibb.co/x35H7bC/2.png",
    "about": "Flautas in a taco story? Absolutely. In Mexico, tacos come rolled as well as folded. And El Paso’s famed rolled tacos—you know the ones!—get justice at this gourmet food truck gone brick-and-mortar inside Funkmeyers Rec Room, an eighties- and nineties-themed “barcade” for nostalgic Gen Xers. (There’s pinball!) The tortillas for the flautas are made from a 50/50 mix of corn masa and white wheat flour, filled with ground beef, formed into flautas, and then fried before being dunked in a tart tomatillo-based salsa verde bath. (Ahogada is Spanish for “drowned.”) Mexican crema amplifies the dish’s sharpness, while queso fresco kicks in with the salt. Also worth consideration is owner Jesse Peña’s interpretation of a Rio Grande Valley taco, shot with queso fresco and a tangle of grilled onions—for those pining for a taste of Brownsville, more than 800 miles away. ",
    "rating":4,
    "reviews": [{ "mark_as_deleted" : False, "review" : "Tacoholics street tacos are everything I have been craving and wanting from street tacos since moving to El Paso. Everything from the tortillas to the meat was loaded with flavor. I also had a cucumber limeade and thought I had died and gone to heaven. I will not be going anywhere else for tacos from now on."}, { "mark_as_deleted" : False, "review" : "Always great food simple and to the point. There isn't anything I don't like on their menu including tofu tacos lol! Only thing I wish is that seating was more comfy so I usually order food to go."},{ "mark_as_deleted" : False, "review" : "Great original and local spot. Been frequenting them for years since they were a food truck.  Always tasty w fresh ingredients.  Their korean style sirloin tacos are my favorite tacos in the EPT!  Killer lunch special served till 3pm."}],
    "location":"1506 N. Lee Trevino (Suite B-1) El Paso Tx, 79936"
    },
    {
    "id": 2,
    "state": "New York",
    "name":"Cesar’s Empanadas",
    "img": "https://i.ibb.co/mJQpztt/3.png",
    "about": "The truck specializes in Latin fare, with a good-sized array of menu choices. The first choice and most recommended are of course, the empanadas. The empanadas are made fresh to order, and you can see how delectable they are just by the tender flakiness of the shell. That taste gets magnified once you bite into it, with all of the savory minced beef, onions and other spices making for a great meal. It’s so good that you will not just have one. Luckily, Cesar’s does have several empanada options like chicken, vegetarian and for you taste thrill-seekers, pizza and lasagna options. And the affordability will let you sample all of these options to your heart’s desire. (Side note for the seafood lovers – yes, they do have a shrimp version.)",
    "rating":4.5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "Cesar's is the fastest and best quick-bite in downtown Brooklyn. Having lived and worked in the neighborhood for 10 years, this place has been a regular place to grab a DELICIOUS and hot 'lunch on the go' or a 'quick bite before going out'. The food is always consistent and well-made, and you always know what you're going to get. Additionally, I once ordered 300 empanadas for a party and the quality was just as superb as ever. My guests were extremely pleased with the food and were scrambling to take the leftovers home with them."}, { "mark_as_deleted" : False, "review" : "Best empanada I've ever had.... Very juicy and was warm when given on a cold cold day! Job well done will definitely come back."},{ "mark_as_deleted" : False, "review" : "This is a great place to stop for some Mexican food downtown. Their tacos are bomb! I've had the chicken, steak and both were delicious. They also have great empanadas. They have one for everyone. I normally get chicken and beef with cheese. Both are amazing! Great snacks if you're looking for something quick. It's also very hot and fresh. They make it to order. All in all good stuff!"}],
    "location":"16-32 Hanson Pl, Brooklyn, NY, 11217"
    },
    {
    "id": 3,
    "state": "Georgia",
    "name": "Tex's Tacos ",
    "img": "https://i.ibb.co/tLwcRVv/4.png",
    "about": "Appropriately dubbed the ‘Antonio Banderas’ of food trucks, the Tex’s Tacos food truck is nothing short of suavé – a fully equipped kitchen & restaurant on wheels. Serving-up a delicious array of ‘Nueva Texicana’ eats with style and grace, we’re bringing the fun & excitement of the Tex’s Tacos experience directly to the people. Keep your head on a swivel, because you never know when the fiesta might roll-up to your neck of the woods! Perfectly cooked tortillas, juicy meat including chorizo, cabeza, and barbacoa, plus *just* the right amount of cotija cheese and cilantro make their $2 (!!!) tacos a must-have. Every day. For the rest of your life.",
    "rating":4,
    "reviews": [{ "mark_as_deleted" : False, "review" : "We just had Tex's Taco Truck serve lunch at our corporate event and it was the hit of the event. Their food was perfectly seasoned. The fries were the bomb, but so were the tacos. I think it was cooked perfectly and the servers were very nice with our customers. It was a perfect choice for us and a great value."}],
    "location":"108 Howell St NE, Atlanta, GA, 30312"
    },
    {
    "id": 4,
    "state": "Chicago",
    "name": "La Cocinita Food Truck ",
    "img": "https://i.ibb.co/Z8JCps6/1.png", 
    "about": "La Cocinita serves different locations every day and are always in demand for catering bookings — probably because their arepas, braised pork, and guasacaca (Venezuelan guacamole) DEMANDS recognition. The arepas were cooked perfectly and crispy enough on the outside but soft and warm on the inside. Seconds are not required, but assumed.",
    "rating":4,
    "reviews": [{ "mark_as_deleted" : False, "review" : "We had our first awesome experience ordering from their food truck at Temperance in Evanston. I can't say anything negative about it. We ordered chicken tacos and lechon arepas along with the rice and beans and boy, were we satisfied! The arepas were cooked perfectly...crispy enough on the outside but soft and warm on the inside. The jalapeño spicy sauce with our chicken tacos was bomb. This will definitely be a regular go-to place for me.""We had our first awesome experience ordering from their food truck at Temperance in Evanston. I can't say anything negative about it. We ordered chicken tacos and lechon arepas along with the rice and beans and boy, were we satisfied! The arepas were cooked perfectly...crispy enough on the outside but soft and warm on the inside. The jalapeño spicy sauce with our chicken tacos was bomb. This will definitely be a regular go-to place for me."}],
    "location":"3700 Orleans Ave New Orleans, LA 70119"
    },
    {
    "id": 5,
    "state": "Texas",
    "name": "Ultimo Taco Truck ",
    "img": "https://i.ibb.co/C2k346V/5.png",
    "about": "Want big flavor without spending big bucks? Look no further than El Ultimo. Tacos start at $1.50 and ratchet all the way up to $1.75 for el ultimo on thick flour tortillas. This place is known for its breakfast taco selection, but you can never go wrong stopping by on your lunch break (shouldn't be hard, their usual spots are right outside the loop). Pick your meat (go for the de chicharron y barbacoa, trust us) and have it topped with salsa verde, grilled onions, cilantro, white cheese, and avocado slices.",
    "rating":4.5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "After a several bad experiences at 'authentic tacos' places I have finally found THE BEST. These people make the most amazing authentic, fresh tacos you can ask for! We are them SO FAST we forgot to take pictures. The meat on the asada tacos was fresh, tender, and perfectly marinated. The 'al pastor' tacos were perfect, as well. The meat was juicy, tender, and had a perfect balance with the marinade. They caramelize the onions they add to all their tacos, and the tortillas are made on the spot! Can't wait to come again!"}, { "mark_as_deleted" : False, "review" : "One of the best taco trucks I've been to. Ordered the barbacoa, fajita, chicharron, and pastor.Barbacoa was awesome, melt in your mouth. Fajita had a great smoky flavor. Pastor had a lot of good pineapple flavor that a lot of other places are missing. Chicharron was okay. Have had better.All the tacos were topped with grilled onions and cilantro. We had them all on corn tortillas as well. They were around $2 per taco and the portion size is a bit bigger than the standard palm size. Can't wait to come back! Can't stop thinking about these tacos."}],
    "location":"7645 Long Point, Houston, TX, 77055"
    },
    {
    "id": 6,
    "state": "Florida",
    "name": "Ay Bendito Con Sabor A Puerto Rico ",
    "img": "https://i.ibb.co/LNrJMTw/6.png",
    "about": "This truck cooks traditional Puerto Rican meals that they hope remind you of your grandmother's dishes — and based on the glowing Yelp reviews, they DO. Savory alcapurrias (meat-filled, fried fritters), tostones rellenos (stuffed fried plantains), and mofongo con camarones (shrimp and plantains) are just some of their many options. It is the real deal!",
    "rating":5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "Hands-down, the best trifongo I ever had. It has been very difficult for me to find some good traditional Puerto Rican food in Miami. I'm so glad to have found this food truck located in Kendall. I swear they have a master's degree in cooking trifongo. Ay Bendito is the real deal! "}, { "mark_as_deleted" : False, "review" : "Amazing food- home cooked with passion you can taste.  Can't wait to see you in Pembroke."}],
    "location":"9225 SW 137th Ave, Miami, FL, 33186"
    },
    {
    "id": 7,
    "state": "Philadelphia",
    "name": "Dos Hermanos ",
    "img": "https://i.ibb.co/92MtKm9/7.png",
    "about": "has become a destination spot for amazing Mexican food, courtesy of their traditional spices and fresh ingredients. It's owned by two brothers, whose passion for bringing their heritage to Philly is clear in their simple yet flavorful tacos (pineapple-marinated pork, anyone?). Definately worth your money!",
    "rating":4.5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "These are by far the best tacos I have found out of a truck in the greater Philadelphia area. Great portions, flavorful meats, and your choice of mild or hot sauce if desired. No mix and match fees for three different tacos always make me more willing to try your food. Other taco trucks, please take notice."}],
    "location":"3397, 3342, 3397, 3366 Market St, Philadelphia, PA, 19104"
    },
    {
    "id": 8,
    "state": "Nevada",
    "name": "Tacos Al Carbon ",
    "img": "https://i.ibb.co/ynqW7bj/8.png",
    "about": "This truck boasts generously sized ~super tacos~ to fill your belly for cheap. $4.99 for a *thicc* burrito that you can order with your choice of meat and beans (including beef tongue)? YES. PLEASE. The food is very flavorful!",
    "rating":4.5,
    "reviews": [],
    "location":"4160 E Sahara Ave, Las Vegas, NV, 89104"
    },
    {
    "id": 9,
    "state": "Michigan",
    "name": "Los Dos Amigos ",
    "img": "https://i.ibb.co/GstkbJC/9.png",
    "about": "Best gem in Michigan. This truck has earned *several* reviews that praise their $2 quesadillas (or you can go for their $1 tacos). You'll get more than bang for your buck — they're generously stuffed with super flavorful meat, cheese, avocado, and spicy pickled onions. Sure, they have a kick to 'em. But it can all be washed down with their horchata.",
    "rating":5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "Oh my gosh. The tacos were SO good. The tortillas really made the taco, too. There were two of them and the bottom one had a crunch to it. I can't even describe it good enough for you to understand! The flavors were amazing. My favorite taco was the pork. Go try this place, you will not be let down!!!"}],
    "location":"7115 Parkwood St, Detroit, MI, 48210"
    },
    {
    "id": 10,
    "state": "Texas",
    "name": "Llalla's Empanadas",
    "img": "https://i.ibb.co/tCRF4bc/10.png",
    "about": "Want some magic inside a pouch? Llalla's uses their family recipes to perfect the art of empanadas: a perfectly fried dough on the outside, and savory mix of meat and spices on the inside. Did I mention they're $4? Or! Try their ~dessert~ empanadas with caramel and apple for $5.",
    "rating":5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "Part of the fun of empanadas is the mystery. The other side of mystery is: you don't know what lies beneath. The sheer joy, though, when there's magic inside the little pouch. The seasoning, the right hints of spice; these are pouches of pleasure! I wanted to try the yuca fries, but was encouraged to get the rice, so I got both — and both are delicious. I usually skip the rice, because it's usually bland filler: not the case here. Yeah, I was having some beers...but I find myself dreaming about those empanadas."}],
    "location":"11911 Crosswinds Way, San Antonio, TX, 78233"
    },
    {
    "id": 11,
    "state": "Florida",
    "name": "El Mambo ",
    "img": "https://i.ibb.co/xYyXMPm/11.png",
    "about": "This one is all about perfection! El Mambo serves crowd-pleasing, absolutely delicious Cuban meals, like the fan-favorite Mambo sandwich with perfectly roasted chicken and garlic aioli. That with a side of congris and plantins = zero possibilities your plate won't be licked clean.",
    "rating":4.5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "I'm so glad I've got to try this food truck. Their food was absolutely delicious! I ordered the ropa vieja, and man, was that heavenly! The meat was so tender and melted in your mouth and the spices were perfection. All of the sandwich components meshed well together as well! It was also massive!"}, { "mark_as_deleted" : False, "review" : "Today, El Mambo was at our offices for lunch.  When I opened my container, I was blown away by the size of the sandwich.  It was literally bigger than my face.  The ingredients were all fresh and hand made.  Not the typical sliced processed meat you get in a sandwich.  The black beans and rice are also amazing.  Reminded me of the Morro I used to get in the Dominican neighborhood I lived in NYC.  These are great guys with an exceptional product.  Can't wait to try something new."}, { "mark_as_deleted" : False, "review" : "I'm so glad I've got to try this food truck. Their food was absolutely delicious! I ordered the ropa vieja, and man, was that heavenly! The meat was so tender and melted in your mouth and the spices were perfection. All of the sandwich components meshed well together as well! It was also massive, so I was only able to eat half of it. It was so worth it though."}, { "mark_as_deleted" : False, "review" : "These guys are amazing! Get a huge, authentic Cuban sandwich for $8? Crazy!  I tried them for the first time at the Fest of Ale, needless to say i was hungry, and even though there was a decent line they got the food out quickly. I was greeted quickly, they took credit cards (bonus) and within minutes I had a HEAVY styrofoam container of Cuban goodness. I could only finish half and saved the rest for dinner. The Cuban community in Louisville is exploding and this truck is a welcome addition. Give them a try!"}],
    "location":"3285 Fraser Ct, Kissimmee, FL, 34746"
    },
    {
    "id": 12,
    "state": "California",
    "name": "Kikos Seafood Lunch Truck ",
    "img": "https://i.ibb.co/gmMMRT3/12.png",
    "about": "Do you want a real fish taco experience? This truck makes the ocean wonder if it has competition for fresher seafood. Best known for its fish tacos, ceviches, and shrimp cocktails, this place will feel so much more expensive than the average $10 you'll spend. Oyster happy hour 'deals'...explain yourselves.",
    "rating":4.5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "Can't beat the price on these amazing fish tacos! I'm even a little hesitant about writing this review, because clearly the secret is out that this is the place to grab a quick, easy, delicious, yummy lunch. I continue comings back here with friends when they want the real fish taco experience. The tacos are fresh, tasty, and sooo good! Highly recommend."}],
    "location":"6090 Friars Rd, San Diego, CA, 92108"
    },
    {
    "id": 13,
    "state": "Massachusetts",
    "name": "North East of the Border ",
    "img": "https://i.ibb.co/pZY7vcx/13.png",
    "about": "Every bite is divine! This truck serves tacos perfected by executive chef, Gustavo Lecanda, who trained in Mexico City before moving to Boston to introduce the city to authentic Mexican cuisine. Each taco recipe is simple but powerful, like the slow-roasted barbacoa taco with marinated brisket, cilantro, and onions on a crisp corn tortilla. You're either drooling or lying.",
    "rating":4,
    "reviews": [{ "mark_as_deleted" : False, "review" : "These tacos sound incredible. But my hungry belly rumbled my answer: The cochinita pibil torta. This magnificent creation is delectably marinated pulled pork with refried beans and pickled onions sandwiched between two slabs of a big, soft, slightly sweet roll. The blending and absorption of filling with bread are divine in every bite, especially when slathered with the flavorful, only-slightly-spicy truck habanero sauce. They cut the torta in half, so theoretically you could save the other piece for later. But I blacked out from sensory overload while eating, and pretty soon the entire thing was gone." }],
    "location":"Rose Kennedy Greenway High St, Boston, MA, 02110"
    },
    {
    "id": 14,
    "state": "Arizona",
    "name": "La Frontera ",
    "img": "https://i.ibb.co/LpmYXPB/14.png",
    "about": "This truck sells street tacos at their vvvvery best. It has reviews that almost all say the same thing: best Mexican food in Arizona. Besides their popular carne asada tacos and huge burritos, the sonoran hot dog is filled to the b-r-i-m with loads of flavor and is WELL worth the $4.50.",
    "rating":4.5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "This is probably supposed to be a secret, but...this is the best Mexican food in Arizona. Yep. Said it. Come here and say otherwise! The carne asada is perfection. The street tacos at their very best. Everything is cooked on the spot. I am so glad I found this place. Any time I'm remotely close, I have to stop and get a taco or burrito."}],
    "location":"209 N 16th St, Phoenix, AZ, 85034"
    },
    {
    "id": 15,
    "state": "California",
    "name": "Sanguchón",
    "img": "https://i.ibb.co/xsRjB6T/15.png",
    "about": "This truck has the best thing you will eat all year. It serves hearty sandwiches and wraps that are generously stuffed with Peruvian ingredients. Stir-fried strip sirloin, free-range chicken, and pulled pork BBQ will MORE than satisfy your belly. You're lying if you say you don't want their fried plantains with chicha sauce on the side.",
    "rating":4,
    "reviews": [{ "mark_as_deleted" : False, "review" : "I had just experienced a thwarted effort in finding something new to eat last Friday, and then on my mopey walk back to the office, I happened upon this truck and took a chance. And yikes! Was I happy! THEIR LOMO SALTADO IS THE BEST THING I'VE HAD TO EAT ALL YEAR! I couldn't recommend it more. It was so good, I brought a buddy back today and got it again! Have mercy!"}],
    "location":"Look at their website for daily locations!"
    },
    {
    "id": 16,
    "state": "New York",
    "name": "Los Viajeros Food Truck",
    "img": "https://i.ibb.co/PgFwwgY/16.png",
    "about": "This one is located in the big apple! It was created by two foodies and self-taught chefs who have already won awards for their flavorful dishes inspired by Dominican, Cuban, and Mexican traditions. Their best-seller: the 'El Jefe burrito' with ropa vieja (cuban-style steak), sweet plantains, montery jack cheese, jalapenos, and chipotle aioli. My stomach is RUMBLING.",
    "rating":4.5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "I ordered the La Flaca burrito and I'm not exaggerating when I say it was the best burrito I've ever had! The chipotle aioli was the perfect balance to the sweet plantains, plus melty cheese and perfectly cooked veggies — to die for! This California native found her spot in NYC."}, { "mark_as_deleted" : False, "review" : "This Cuban inspired taco/tortilla/etc. truck comes near Bellevue once a week (well on 29th in that weird Alexandria area.) I've ordered the El Jefe which is excellent. I'd prefer if the maduros were a bit sweeter but the beef is quite good and the sandwich has a good light kick from the jalapenos. Nice staff."}],
    "location":"Look at their website for daily locations!"
    },
    {
    "id": 17,
    "state": "Louisiana",
    "name": "Rollin' Fatties",
    "img": "https://i.ibb.co/BVKCtnN/17.png",
    "about": "Rollin' Fatties mixes and matches a core of ingredients, such as jerk seasoned tofu, caramelized tilapia, chipotle cream or Monterey Jack cheese, to build four hefty items: 'fattie' burritos, rice bowls, tacos and nachos. What Rollin' Fatties cooks -- sweet, salty and filling -- has the anything-goes-creativity of an enthusiastic tailgate chef. Although they now cook fish and chicken, red meat is still banished from their kitchen. 'I felt like the food trucks overlook the vegetarians and vegans,' said Zella Daste, one of the owners and a vegetarian himself. 'Most restaurants do too.'",
    "rating":5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "Holy mother of burritos! I've been deprived of good Mexican food/burritos since I've relocated to New York but hot dayuuum, Rollin' Fatties is on my list of NOLA #GOAT. Rightfully named, these bad boys are FATTIES and stuffed to the max! It's a miracle they don't come bursting out of their tortilla wrap. There was just enough pico de gallo without it being too soggy. The seasoned basmati rice was light, soft, and seriously flavorful. The red cabbage slaw had a heavenly pickle and honestly, I couldn't decide if I liked the rice, slaw, or protein more. The chipotle cream just tied everything together into a juicy, southern creole Studio 54 dance party that I want to be a part of forever. Burrito-blessed in New Orleans."}, { "mark_as_deleted" : False, "review" : "I came here on my lunch break because I heard it was really good. I was not disappointed. It was delicious. I had a Fatties bowl and i was blown away by how amazing it was."}],
    "location":"1430 Tulane Ave, New Orleans, LA, 70112"
    },
    {
    "id": 18,
    "state": "California",
    "name": "El Chato Taco Truck",
    "img": "https://i.ibb.co/0JQB4ZY/18.png",
    "about": "One of the best experience over here in LA. Chatos is amazing food truck. THE SELL QUALITY. Tacos are really great but burritos are next level. Services is fast but guys this place is always busy so you have to wait for your food but it worthy",
    "rating":4.5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "I felt strongly compelled to write an update to my review from three years ago, because two sentences does not do this truck justice. I've been eating at El Chato for three years now — trekking all across LA from Pasadena just for some tacos. When I first started coming here, I was vegetarian, and now vegan, I still can get my grub on here (shout out to El Chato for being one of the only authentic trucks with veggie options around). These tacos are incredible. I don't know what kind of salsa they use, but it's the best veggie taco I've ever had. Who would have ever thought that rice and beans on a tortilla could be SO satisfying? Top with your favorite salsa (mine's green) and some lime, and go to town!"}, { "mark_as_deleted" : False, "review" : "I don't live in LA but I have driven to LA solely for this place. Their tacos are so juicy and flavorful, it's like a mouthful of goodness. Their horchata was very sweet and even for a taco truck, they don't skimp out on anything...everything I go, they never disappoint!Great for a late night meal after the club or just hanging with friends! And I believe the prices are super cheap too! Love this place!"}],
    "location":"5300 W Olympic Blvd, Los Angeles, CA, 90019"
    },
    { 
    "id": 19,
    "state": "New Mexico",
    "name": "Taco Bus",
    "img": "https://i.ibb.co/m6S0Gkf/19.png",
    "about": "Everyone talks about the Taco Burger! This delicious truck serves while you sit (wait for it) on the bus! Besides the unique ~dining experience~, the tacos do NOT disappoint with their super fresh salsa and perfectly-cooked meat. Feeling adventurous? Try their taco burger.",
    "rating":4.5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "This is the only place I've seen El Yucateco sauce on the table! I'm already a huge fan, loved the food and service and ambience. Never eaten on a bus but it feels so right! I'm so surprised, I haven't eaten here before and will totally come back asap! The el pastor was delicious, my friend's asada quesadilla looked bomb, and the taco burger blew my mind. I need to eat MORE, but my body needs a break, lol."}, { "mark_as_deleted" : False, "review" : "The Taco Bus is a unique restaurant.   They have full service dining in a converted city bus.   The food is excellent.I got the Fuego burger"}],
    "location":"4801 Central Ave NW, Albuquerque, NM, 87105"
    },
    { 
    "id": 20,
    "state": "Oregon",
    "name": "Tehuana Oaxacan Cuisine",
    "img": "https://i.ibb.co/59X1C4p/20.png",
    "about": "This place combines the comfort of Mexican home-cooked meals with dishes meant to i-n-h-a-l-e. Come for savory tlayuda, filling entomatadas, and amazingly generous burritos.",
    "rating":5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "I missed home so I came here to see if I could satisfy my craving for authentic food. This place is a gem...down home cooking and fair pricing!! I grabbed the enchiladas and the chicken and al pastor tacos. They were fresh and delicious, and there are other carts that sell alcoholic drinks if you want to enjoy a beer with your tacos."}],
    "location":"1331 N Killingsworth St, Portland, OR, 97217"
    },
    {
    "id": 21,
    "state": "Virginia",
    "name": "Tacos El Chilango",
    "img": "https://i.ibb.co/BgHMxQB/Screen-Shot-2020-03-12-at-1-43-09-AM.png",
    "about": "This place can always be found with a loyal line of people waiting for their share of delectable, fresh tacos. DELICIOUS BTW! The portions are generous, the meat oh-so-perfectly cooked, and their salsa selection adds a welcome KICK. Basically, your lunch breaks should exclusively be taken here.",
    "rating":4.5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "THESE TACOS ARE SOOOO LEGIT!! I recently went to Tijuana, Mexico to try their tacos while I was in San Diego for a trip. The tacos from El Chilango taste EXACTLY like the ones I had in Mexico. I love the chorizo and mixto ones the best."}, { "mark_as_deleted" : False, "review" : "Real Mexican tacos!!! Really hard to find in the area, I only know of two place where they make genuine Mexican tacos.The tacos here are amazing and the owner is really friendly!!I highly recommend"}],
    "location":"1723 14th St N, Arlington, VA, 22209"
    },
    {
    "id": 22,
    "state": "Tennessee",
    "name": "5Points Tacos",
    "img": "https://i.ibb.co/KhfjD72/22.png",
    "about": " 5Points Tacos is considered a must-have by locals who go back again (and again) for the superb breakfast tacos, tamales, huge tortas, and MORE. Much More! And, of course, the traditional tacos always hit the spot with perfectly cooked tortillas, flavorful meat like tongue, shrimp, and pork, and their spicy green sauce. Should def be in your bucket list!",
    "rating":4.5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "I don't know why it's taken us so long to try Five Points Tacos! We just finished our second round in two days and we're over the moon. My husband and I are from Southern California and have spent our last six years in Nashville searching for a taco spot that reminds us of home. The tortillas are perfect, their meats are delicious, and their salsas are on point. So stoked about this place and I can't say enough great things."}],
    "location":"1101 Woodland St, Nashville, TN, 37206"
    },
    {
    "id": 23,
    "state": "California",
    "name": "The Lobos Truck",
    "img": "https://s3-media0.fl.yelpcdn.com/bphoto/FutEakoNao0n2cminO12eQ/o.jpg",
    "about": "LA's #1 Gourmet Food Truck. They serve classic American comfort food with a twist. They use quality meats, organic produce and lots of flavor in every heartwarming dish. Their menu includes our famous WACHOS, mac & cheese, burgers, baby back ribs and wings. What is a Wacho? The word wacho comes from waffle fries and nacho. They use criss cut potato fries (waffle fry) and top them with nacho toppings.",
    "rating":4.5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "The prompt customer service and excellent attention to detail makes Lobos an excellent choice for your event! They were personable and willing to work with our specific requirements on a very tight timeline. Very much appreciated!"}],
    "location":"Check out their Website for the Location!"
    },
    {
    "id": 24,
    "state": "California",
    "name": "Sus Arepas",
    "img": "https://s3-media0.fl.yelpcdn.com/bphoto/tLFu0vLMuk6WQaj4I5HDuA/o.jpg",
    "about": "Sus Arepas is the culmination of Colombian tradition and Los Angeles culture coming together to bring a food experience unique to an already very diverse L.A. food market. The Arepas have won awards! Made by the best! Should be on your bucketlist to try!",
    "rating":4,
    "reviews": [{ "mark_as_deleted" : False, "review" : "Best Arepas I have ever had!"}],
    "location":"Check out their Website for the Location!"
    },
    {
    "id": 25,
    "state": "California",
    "name": "Super Tortas DF",
    "img": "https://i.ibb.co/mG9B9wX/24.png",
    "about": "Listen. This is the spot. If you want a true, authentic LA food truck experience THIS IS IT. One of the best sandwiches in all of the city, the Cuban Torta reigns supreme. Watch them delicately cook your sandwich in pure awe, and when your moment of truth comes and they deliver their masterpiece into your grimey hands you will be thankful. Like spice? You're damn right you like spice. Get the chiles on it. Add the sauce they give you. Don't like spice? Well then don't do that but add some pineapple to it. There's a way for everyone to be happy here. So what are you waiting for just go and experience the magic",
    "rating":4.5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "The tortas are so good here haven't been here In a good minute.Friendly service and they don't skimp out on the contents of your food here it's a must when I'm in town."}, { "mark_as_deleted" : False, "review" : "I love tortas so you know I had to check this place out. I actually ate tacos right before coming here so I will def have to come back again to try out the other tortas on an empty stomach."}],
    "location":"Check out their Website for the Location!"
    },
    {
    "id": 26,
    "state": "California",
    "name": "Pablito's Tacos",
    "img": "https://i.ibb.co/LP5DnMV/25.png",
    "about": "In December 2018, Danny Rodriguez and Chef Flor Oropeza decided to merge their two culinary passions into the creation of PABLITO’S Tacos. Their tacos would have the hand made tortillas , mesquite grill and free guacamole for that Tijuana explosive flavor, along with the Peruvian touch. One stand in the parking lot of PABLITO’s kitchen and the rest is history. PABLITO’s tacos specializes in Tijuana Style tacos with a Peruvian touch. All come with handmade tortillas and free guacamole. ",
    "rating":4,
    "reviews": [{ "mark_as_deleted" : False, "review" : "If Ceviches could feel, this ceviche would totally make the other ones jealous. Typing as I'm digesting the best thing ever"}, { "mark_as_deleted" : False, "review" : "I love this place,  came here my first time today got the asada tacos. They are super delicious I love how the meat is cooked it is rich in flavor and full of so much love I highly recommend this place to anyone looking to taste some amazing food!"}],
    "location":"Check out their Website for the Location!"
    },
    {
    "id": 27,
    "state": "California",
    "name": "Tender Grill Gourmet Brazilian Kitchen",
    "img": "https://i.ibb.co/SRzcH2k/27.png",
    "about": "The first gourmet Brazilian food truck in the City of Angels offers Angelenos Brazilian appetizers like Pao de Quiejo (cheese bread), salads featuring picanha (steak), sandwiches like Catupireza Sandwich (smoked Brazilian sausage). It also has  traditional gluten-free Brazilian plates like Herb Marinated Chicken Breast with farofa, and desserts like Mousse de Maracuja (passion fruit mousse). Worth a Try! You will not regret it!",
    "rating":4.5,
    "reviews": [{ "mark_as_deleted" : False, "review" : "All I have to say is that you can't go wrong with either of these dishes. The cheese bread was so delightful to my palate. I took one  bite and there was so  much soft cheese just oozing out of it. The Catupireza Sandwich is no joke.  That is a to die for type of sandwich. I'm talking next level. It's just filled with so much goodness like smoked Brazilian sausage, gourmet Brazilian catupiry cheese, mushrooms, potato sticks, grilled red onions, and roasted garlic aiolii on a slightly toasted brioche with fries. Now doesn't that sound appealing for meat  lovers? My friend had the Steak  salad and loved it. It's  definitely worth  trying. I'll be coming back  for more."}, { "mark_as_deleted" : False, "review" : "The Tender Grill truck came to our apartment complex tonight, so we decided to try it. My hubby had the steak bowl, which was tender, flavorful, and perfectly cooked. I tried the Chicken Stroganoff bowl, and all I can say is 'Wow!' The white meat chicken was very tender, and the  creamy tomato sauce was delicious. The crispy potato sticks were a nice crunchy addition. Definitely looking forward to patronizing them again."}],
    "location":"12402 Washington PIace Los Angeles, CA 90066"
    },
    {
    "id": 28,
    "state": "Texas",
    "name": "Azucar",
    "img": "https://i.ibb.co/tzHPfw6/28.png",
    "about": "According to Roaming Hunter, Azucar is one of Dallas’ best kept secrets. With lunch menu offerings like Mayan Taco (frybread topped with beans, rice, an assortment of veggies, and your choice of meat) and loaded burritos, it’s easy to understand why locals would want to keep this Latin food truck to themselves. You will love it! I promise!",
    "rating":4,
    "reviews": [{ "mark_as_deleted" : False, "review" : "Amazing food great taste. Their salsa is awesome great portions would definitely try again and recommend."}, { "mark_as_deleted" : False, "review" : "I was pleasantly surprised to see a vegan option, the veggie tacos sans dairy. They were SO good. The sauce had a nice balance of heat and flavor, and the tortillas were fried nicely. I wished I could have more."}],
    "location":"8950 Cypress Waters Blvd Irving, TX 75063"
    },
    {
    "id": 29,
    "state": "Arizona",
    "name": "Que Sazon",
    "img": "https://i.ibb.co/q9X15f1/29.png",
    "about": "The name says it all! SEASONING OUT OF THIS WORLD! If South American cuisine is what you’re craving, this Phoenix truck should be on your list of great Latin food trucks. Serving Latin-inspired food like chicken empanadas, a side of sweet plantains, and arroz con pollo (classically Latin!), Que Sazon will meet all your street food requirements.",
    "rating": 4.5,
    "reviews": [ { "mark_as_deleted" : False, "review" : "So glad this food truck had a tofu bowl!!! And it was so amazing! The tofu and veggie rice bowl came with rice and beans, topped with grilled tofu, veggies. The food was really good and not spicy at all, I did end up adding a a lot of hot sauce to my bowl but it's great for anyone who doesn't want too much spice in their food. My colleagues tried the pork and chicken bowls and they totally loved them as well. Portion is good for one person, it does leave you full to the neck. Their fries are amazing as well and come with toppings of your choice. Totally recommend it!"}, { "mark_as_deleted" : False, "review" :  "I have bought food from this food truck twice at two different events. 1st @ Foodstock & 2nd @ Food Truck Friday's at Pioneer Park. Both times I have enjoyed their food.I recommend getting the Fries topped with pork (chicken was good too, but the pork was more flavorful). My wife and I really enjoyed them! Looking forward to having it again!"}],
    "location":"Check out their Website for the Location!"
    }
]

# method used to renumber the ids of elements within the data 
def renumber(data):
    for i in range(0,len(data)):
        data[i]['id'] = i

# render home page 
@app.route("/", methods=['POST','GET'])
def render_home_html():

    global food_trucks
 
    latest_entries = [ t for t in reversed(food_trucks[-12:])]
    
    return render_template('home.html', latest_entries = latest_entries)

# search for data based on query 
@app.route("/search_query/<query>", methods=['POST','GET'])
def search_query(query):

    global food_trucks

    query_1 = str(query.lower())
    
    query_results = []
    for data in food_trucks:

        state = data['state'].lower()
        name = data['name'].lower()
        about = data['about'].lower()

        if (query_1 in state) or  (query_1 in name) or (query_1 in about) :
            query_results.append(data)
    
    
    return render_template('search_results.html', query_results = query_results, query_1 = query)

# create data 
@app.route("/create", methods=['POST','GET'])
def render_create_html():

    if request.method == 'POST':

        global food_trucks

        json_data = request.get_json()

        new_id = len(food_trucks)

        new_entry = {
            "id": new_id,
            "state" : json_data['state'],
            "name" : json_data['name'],
            "img" : json_data['img'],
            "about" : json_data['about'],
            "rating" : json_data['rating'],
            "reviews" : [{ "mark_as_deleted" : False, "review" : json_data['review']}],
            "location" : json_data['location']
        }

        food_trucks.append(new_entry)

        return jsonify(new_id=new_id)
    else:
        return render_template('create.html')

# view data 
@app.route("/view/<id>", methods=['POST','GET'])
def view_food_truck(id=id):

    global food_trucks

    food_truck_data = food_trucks[int(id)]

    return render_template('view.html', food_truck_data=food_truck_data) 

# update the location data if the user edits it 
@app.route("/view/update_location", methods=['POST','GET'])
def update_location():

    global food_trucks

    json_data = request.get_json()

    location = json_data['location']
    truck_id = json_data['id']

    food_trucks[int(truck_id)]['location'] = location

    return jsonify(truck_id=truck_id)

# update the review data if the user deletes it 
@app.route("/view/update_comment", methods=['POST','GET'])
def update_comment():

    global food_trucks

    json_data = request.get_json()

    truck_id = json_data['truck_id']
    comment_id = json_data['comment_id']
    delete_comment = json_data['delete_comment']
    if delete_comment == True:
        food_trucks[int(truck_id)]['reviews'][comment_id]['mark_as_deleted'] = True
    else:
        food_trucks[int(truck_id)]['reviews'][comment_id]['mark_as_deleted'] = False


    return jsonify(truck_id=truck_id)

# add a review if the user adds one 
@app.route("/view/update_review", methods=['POST','GET'])
def update_review():

    global food_trucks

    json_data = request.get_json()

    review = json_data['review']
    truck_id = json_data['id']

    food_trucks[int(truck_id)]['reviews'] = [{ "mark_as_deleted" : False, "review" : review}] + food_trucks[int(truck_id)]['reviews']

    return jsonify(truck_id=truck_id)


if __name__ == '__main__':
    app.run()
