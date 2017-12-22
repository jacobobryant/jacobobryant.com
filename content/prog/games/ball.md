+++
title = "Games"
+++

In my [ball.html](/ball.html) program, the HTML says that there should
be an area to draw graphics on (called a canvas) and that there
should be a bit of text that says "Use the arrow keys to move the
ball." The CSS says that the canvas should have a border around it and
that the text should be at the top left of the screen, on top of the
canvas. The Javascript controls the ball.

If you view the page source (if you're using Chrome, go to
[ball.html](/ball.html) and then hit Control-U), you'll find this bit
of code about halfway down:

```javascript
function update() {
  resize_canvas();
  gravity();
  thrust();
  friction();
  move();
  collision();
  draw();
}
```

This code is ran every 15 milliseconds. It takes the ball's current
position and velocity and then simulates gravity, user input and
friction to calculate where the ball should be next. If the ball
collides with a wall, it'll handle that too.
