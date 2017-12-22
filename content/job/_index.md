## Part-time job opportunity for BYU students
PIPE is a prototype app being built as part of a collaboration
agreement between a large company and BYU. The project is meant to be
a meaningful learning experience for students as they work on a team
with peers and mentors to help solve a real industry problem. Areas of
work include:

 - machine learning
 - natural language processing
 - mobile & web app development
 - server (Linux) administration

We're looking to hire a few people who have experience in these topics
or who want to learn about them. If you're interested in the project,
send me an email at
[foo@jacobobryant.com](mailto:foo@jacobobryant.com). I'm happy to
answer any questions you have or give you more information about the
project in general.

### Project description
I've been working on PIPE for the past few months. It's an automatic
todo list manager. What sets this apart from other todo list apps is:

 - It will use natural language processing to parse features from
   input text, e.g. priority, deadline, time required to complete
   task.
 - It will learn a scoring function to automatically sort the tasks
   based on those features.
 - When using the app, the user simply gives the number of minutes
   they have to work on something. The app gives them the best task to
   do given that time.

Example use case: a busy project manager has 15 minutes to spare in
between meetings. Instead of losing 5 minutes finding a task to work
on, they pull out their phone, enter "15" into the app and then
they're presented with "email John Smith about the frobulator".

I've written and deployed a basic [web](https://pipe.jacobobryant.com)
+ [mobile\*](https://jacobobryant.com/pipe.apk) app, but we currently
have only simple proof-of-concept functions for parsing input text and
scoring tasks. The next phase of the project is mainly to implement
the parsing and scoring functions using NLP/ML. Also we'll deploy the
app within the company and start gathering usage data from it. We'll
use that data to train the scoring function.

\*I've only packaged the mobile app for Android so far, but we'll have
an iOS version soon.

### Our needs
We especially need someone who can do the NLP/ML parts. You don't have
to be an expert as long as you have a sufficiently solid background so
that you can learn as you go and be productive. But there are other
parts of the project to work on if you haven't done NLP/ML before.
We're looking for people at all levels of experience.

You will need to be comfortable working with minimal supervision. I
will have only ~3 hours to work on the project after I start a
full-time job in January. I'll mainly be available as a mentor. (Also
my main ML experience is just CS 478, so I'm no expert myself). My
supervisor is extremely busy and only has time for a video call every
few weeks. We have ideas about how to move forward with the project,
but we need you to help figure it out as we go.

A minimum of 10 hours/week would probably be best, but we likely could
make use of 15-20 if you can do it.

### Benefits
 - Learning. This is a great opportunity to get hands-on experience.
 - Creative freedom. You won't be just a code monkey.
 - Flexible schedule. You'll clock in with ytime (which is accessible
   from my.byu.edu) but you can work wherever and whenever you want.
 - Startup opportunities. If our prototype works well, the company may
   provide funding for a startup to fully develop the app and deploy
   it for all their employees.

Pay depends on experience.

### Current project architecture
The backend is a set of Docker containers (Clojure web app, Nginx,
Postgres) running on a Digital Ocean droplet. The frontend is written
with React Native and Clojurescript, so it's cross-platform (but we
mainly just need the iOS version because that's what the company
uses).

This architecture isn't set in stone, but I include it to give you
more of a feeling for the project.
