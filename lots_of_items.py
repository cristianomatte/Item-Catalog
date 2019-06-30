#!/usr/bin/env python3

from repository.sqlite import db_session, create_database
from model.user import User
from model.category import Category
from model.item import Item


create_database()

# Create football category and its items
football = Category(name='Football')
db_session.add(football)
db_session.commit()

description = ('Footballers wear lightweight, comfortable and durable shoes '
               'that are usually studded to provide good grip on muddy or '
               'slippery surfaces.')
shoes = Item(name='Shoes', description=description, category=football)
db_session.add(shoes)
db_session.commit()

description = ('Goalies are allowed to wear headgears during the play though '
               'it is not mandatory, but many of them opt for it as it '
               'protects them against any head injury.')
goalie_gloves = Item(name='Goalie Gloves',
                     description=description,
                     category=football)
db_session.add(goalie_gloves)
db_session.commit()

description = ('This protective equipment is worn by players and the goalie '
               'to protect their shin bone from any injury.')
shin_guard = Item(name='Shin Guard',
                  description=description,
                  category=football)
db_session.add(shin_guard)
db_session.commit()

description = ('Balls are made from synthetic material that has a '
               'circumference of 68 to 70 cm, weighs around 410 to 450 grams '
               'and has inflation pressure between 600 to 1100 g/sq. cm. at '
               'sea level. These balls have a covering of synthetic leather '
               'panels stitched together and have latex or butyl air bladder '
               'inside.')
football = Item(name='Football', description=description, category=football)
db_session.add(football)
db_session.commit()

# Create volleyball category and its items
volleyball = Category(name='Volleyball')
db_session.add(volleyball)
db_session.commit()

description = ('Padded elbow guards are worn to protect the elbow from '
               'injuries during a fall or a strike.')
elbow_pads = Item(name='Elbow Pads',
                  description=description,
                  category=volleyball)
db_session.add(elbow_pads)
db_session.commit()

description = ('Protective kneepads may be worn by players for prevention '
               'against grazing.')
knee_pads = Item(name='Knee Pads',
                 description=description,
                 category=volleyball)
db_session.add(knee_pads)
db_session.commit()

description = ('A net divides the volleyball court into two halves, through '
               'which the players of the opposing teams pass the ball. '
               'Different size of the net is used for male and female games '
               'respectively.')
net = Item(name='Net', description=description, category=volleyball)
db_session.add(net)
db_session.commit()

description = ('A spherical, leather or synthetic leather ball is used that '
               'has a circumference of 65-67 cm, weighs around 260-280 grams '
               'with an inside pressure of 0.30-0.325 kg/sq. cm. Volleyball '
               'consists of eighteen small-sized panels of leather arranged '
               'in six equal sections that are wrapped around a bladder.')
volley_ball = Item(name='Volley Ball',
                   description=description,
                   category=volleyball)
db_session.add(volley_ball)
db_session.commit()

# Create swimming category and its items
swimming = Category(name='Swimming')
db_session.add(swimming)
db_session.commit()

description = ('Swimmers wear specially designed swimsuits made of latex, '
               'nylon or Spandex materials. The right swimsuit should fit the '
               'body and doesn’t hinder the movement. According to FINA '
               'regulations, men’s suits should not cover their knees and '
               'navel and women’s one-piece suits must leave their neck, '
               'shoulders and knees uncovered.')
swim_suit = Item(name='Swim Suit', description=description, category=swimming)
db_session.add(swim_suit)
db_session.commit()

description = ('Goggles are used during swimming to keep water and chlorine '
               'out of the swimmer\'s eyes.')
goggles = Item(name='Goggles', description=description, category=swimming)
db_session.add(goggles)
db_session.commit()

description = ('Swim caps are usually worn by long haired swimmers to '
               'protect their hair from chlorinated water and to reduce drag '
               'in the water caused by loose hair.')
swim_caps = Item(name='Swim Caps', description=description, category=swimming)
db_session.add(swim_caps)
db_session.commit()

# Create snowboarding category and its items
snowboarding = Category(name='Snowboarding')
db_session.add(snowboarding)
db_session.commit()

description = ('The device that connects/binds a ski boot to the ski is '
               'known as a binding. It fixes the boot at the toe and heel.')
bindings = Item(name='Bindings',
                description=description,
                category=snowboarding)
db_session.add(bindings)
db_session.commit()

description = ('It is made of hardwood core with fiberglass lamination. '
               'Freestyle boards are comparatively short and flexible with a '
               'symmetrical nose and tail while alpine boards are longer, '
               'narrow and rigid with a distinct front and back. The edges of '
               'the boards are symmetrically curved that assist in turning.')
snowboard = Item(name='Snowboard',
                 description=description,
                 category=snowboarding)
db_session.add(snowboard)
db_session.commit()

description = ('Skiers wear a helmet with padded chin-strap that covers the '
               'head and ears and consist of a hard plastic or resin shell '
               'with inner padding to withstand several impacts and gives '
               'warmth and extra protection for the head.')
helmet = Item(name='Helmet', description=description, category=snowboarding)
db_session.add(helmet)
db_session.commit()

description = ('Soft and flexible boots are worn during freestyle '
               'snowboarding. This boot slows the transmission of body '
               'movement to the board. Hard boots with the rigid shell are '
               'worn in alpine snowboarding. This boot allows for the '
               'immediate transmission of body movement to the board.')
boots = Item(name='Boots', description=description, category=snowboarding)
db_session.add(boots)
db_session.commit()

# Create lacrosse category and its items
lacrosse = Category(name='Lacrosse')
db_session.add(lacrosse)
db_session.commit()

description = ('Sticks made of wood, plastic or composite material are used '
               'in lacrosse having the length of 40-42 inches for attackers, '
               '52-72 inches for defensemen and 40-72 inches for the goalies. '
               'Plastic molded head of the stick has nylon, linen or leather '
               'pocket. The head can be maximum 10 inches wide for each '
               'player except the goalie (much larger head with maximum 12 '
               'inches width). The pocket of the Crosse must not be deeper '
               'than the diameter of the ball.')
stick = Item(name='Stick', description=description, category=lacrosse)
db_session.add(stick)
db_session.commit()

description = ('A white, yellow or orange colored, solid rubber ball is used '
               'in lacrosse having the circumference between 7.75-8 inches '
               'and weighing around 5-5.5 ounces.')
ball = Item(name='Ball', description=description, category=lacrosse)
db_session.add(ball)
db_session.commit()

description = ('Except for the goalie, all players of the men’s lacrosse '
               'team wear shoulder guards for protection against injuries.')
shoulder_guard = Item(name='Shoulder Guard',
                      description=description,
                      category=lacrosse)
db_session.add(shoulder_guard)
db_session.commit()

# Create rugby category and its items
rugby = Category(name='Rugby')
db_session.add(rugby)
db_session.commit()

description = ('The goal is a crossbar in H-shaped form. The goal is scored '
               'by kicking or dropping the ball over the crossbar.')
goal_post = Item(name='Goal Post', description=description, category=rugby)
db_session.add(goal_post)
db_session.commit()

description = ('A rugby ball is an oval-shaped ball made of leather or '
               'synthetic material that is composed of four leather panels '
               'stitched together. It has a length of 28-30 cm, an end-to-end '
               'circumference of 74-77 cm and in-width circumference of 58-62 '
               'cm. The ball weighs between 410-460 grams.')
ball = Item(name='Ball', description=description, category=rugby)
db_session.add(ball)
db_session.commit()

description = ('The players wear lightweight helmet or skullcap made of '
               'shatter-resistant plastic to protect them in the scrum.')
skullcap = Item(name='Skullcap', description=description, category=rugby)
db_session.add(skullcap)
db_session.commit()

description = ('Very similar to the football shoes, the rugby players wear '
               'shoes with cleated soles that provide support to the ankle. '
               'The cleats must not exceed 18mm in length.')
shoes = Item(name='Shoes', description=description, category=rugby)
db_session.add(shoes)
db_session.commit()

# Create tennis category and its items
tennis = Category(name='Tennis')
db_session.add(tennis)
db_session.commit()

description = ('Yellow or white-colored balls weighing around 2.5 ounces with '
               'a diameter of 2.5 inches are used. It consists of a core made '
               'of a cork wrapped in fabric tape with a covering of hand-sewn '
               '“Melton” cloth. Real tennis balls are heavier and less bouncy '
               'than lawn tennis balls.')
ball = Item(name='Ball', description=description, category=tennis)
db_session.add(ball)
db_session.commit()

description = ('The net is approximately 5 feet high at the sides and around '
               '3 feet at the center.')
net = Item(name='Net', description=description, category=tennis)
db_session.add(net)
db_session.commit()

description = ('Wooden racquets with a length of 27 inches are used that '
               'have very tight strings to cope with the heavy balls. The '
               'heads of the racquets are angled slightly to make it possible '
               'to play shots close to the floor or in the corners.')
racquet = Item(name='Racquet', description=description, category=tennis)
db_session.add(racquet)
db_session.commit()

description = 'Players wear wristbands to wipe perspiration from their face.'
wristbands = Item(name='Wristbands', description=description, category=tennis)
db_session.add(wristbands)
db_session.commit()

# Create curling category and its items
curling = Category(name='Curling')
db_session.add(curling)
db_session.commit()

description = ('Broom is used to sweep/melt the ice in the stone’s path and '
               'also used as a balancing aid. The handle of the brooms are '
               'hollow tubes made of carbon fiber or fiberglass and are '
               'lighter and stronger that allows fast sweeping.')
broom = Item(name='Curling Broom', description=description, category=curling)
db_session.add(broom)
db_session.commit()

description = ('Stone made of granite is used in curling that weighs around '
               '17.24-19.96 kg, has a circumference up to 36 inches and a '
               'minimum height of 4.5 inches. The running surface (bottom of '
               'the stone) of the stone is 6-12 mm wide and is about 5 inches '
               'in diameter.')
stone = Item(name='Curling Stone', description=description, category=curling)
db_session.add(stone)
db_session.commit()

description = ('It may be used by curlers to time the stone over a fixed '
               'distance. It may be attached to the clothes or the broom.')
stopwatch = Item(name='Stopwatch', description=description, category=curling)
db_session.add(stopwatch)
db_session.commit()

description = ('Curler’s shoes have different soles. A “slider” with a smooth '
               'sole is worn on the lead foot and the “gripper” is worn on '
               'the hack foot to grip the ice during delivery of the stone.')
shoes = Item(name='Shoes', description=description, category=curling)
db_session.add(shoes)
db_session.commit()

# Create Kung Fu category and its items
kung_fu = Category(name='Kung Fu')
db_session.add(kung_fu)
db_session.commit()

description = ('These are used to protect the front of the torso against '
               'hard blows.')
chest_protector = Item(name='Chest Protector',
                       description=description,
                       category=kung_fu)
db_session.add(chest_protector)
db_session.commit()

description = ('Gloves are made of an outer layer of leather, stitched with '
               'nylon thread, and padded with high-density polyurethane.')
gloves = Item(name='Gloves', description=description, category=kung_fu)
db_session.add(gloves)
db_session.commit()

description = ('Groin protectors are worn by most of the athletes for '
               'protection against injuries.')
groin_protector = Item(name='Groin Protector',
                       description=description,
                       category=kung_fu)
db_session.add(groin_protector)
db_session.commit()

description = ('A mouth guard is used to reduce the risk of damage from a '
               'kick to the face.')
gum_shield = Item(name='Gum Shield', description=description, category=kung_fu)
db_session.add(gum_shield)
db_session.commit()

description = ('Athletes wear head guards to prevent any head injuries '
               'because in this sport, blows to the head are allowed.')
head_protector = Item(name='Head Protector',
                      description=description,
                      category=kung_fu)
db_session.add(head_protector)
db_session.commit()

print('Successfully created categories and items!')
