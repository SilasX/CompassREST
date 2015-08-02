# About

Compass RESTful endpoints added during AngelHacks Hackathon, August 1, 2015.

Basic REST setup forked from [Derek Adair's ](https://github.com/derek-adair/django-rest-docker).

# Compass Project Links

[Main Compass project page](http://compass-angelhack.meteor.com)

[Website implementing this REST backend](http://compassangelhack.silasbarta.com/)

[Android client code](https://github.com/tsato1/Compass-Android)

[iOS client code](https://github.com/JCheungX/CompassIOS)

# Models

This backend implements the following models:

## Product

Some kind of excess inventory that is being sold, with a name, description, and offered price, owned by a Group.

## SellListing

Some offer to sell a product, by a seller (instance of User model), and how much they have available.

## Users

Registered users who can be sellers of objects.

## Group

Can be an owner of a Product.

## Location

Where the products are being sold; a sell listing can connect to it.

# Running locally

django rest framework ready to rock and roll with fig+docker

    docker-compose build web
    docker-compose run web migrate
    docker-compose up
    #in another terminal
    docker-compose run web syncdb
