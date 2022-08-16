# union_avatars_test


## Build an API
We’d like to build a website that anyone can use to retrieve information about Autonomous
System (AS) providers. Your task is to build the API that the website will use.
To power the API, you can use the database offered at: https://iptoasn.com/. You need to
download their database and load it into your API.


Requirements:

  ●The API needs to have, at least, the following endpoints:

    ○Given an AS number, return the AS information

    ○Given an IP address (v4 or v6), find the AS that owns the network that the IP
      belongs to, and return the AS information
  ●Use SQLite to store the AS information

  ●Use Python as the programming language and any framework that you’d like.

  ●Test the application. No need to have 100% coverage, but tests should show what
  and how you would test the different parts of your application


Bonus points:

  ●Containerize the application so it is straightforward to run!


## ENDPOINTS
  get_as_information(as_number)
  get_as_network_owner(ip)


## TSV FORMAT
range_start

range_end

AS_number

country_code

AS_description
