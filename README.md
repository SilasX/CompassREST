Forked from [Derek Adair's ](https://github.com/derek-adair/django-rest-docker).

Compass RESTful endpoints added during AngelHacks Hackathon, August 1, 2015.


# Running locally

django rest framework ready to rock and roll with fig+docker

    docker-compose build web
    docker-compose run web migrate
    docker-compose up
    #in another terminal
    docker-compose run web syncdb
