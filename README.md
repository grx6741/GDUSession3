# GDUSession3

## Python VS C

> for loops

```python
# python

# range based loop
for i in range(first, last + 1):
    print(i)

# iteratory loop
nums = [1, 4, 6, 2, 3]
for num in nums:
    print(num)
```

```c
// C
for (int i = first; i < last; i++) {
    printf("%d\n", i);
}
```

> while loops

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

```c
int i = 0;

while (i < 10) {
    i++;
    printf("%d\n", i);
}
```

> Pygame vector methods

```python
vec = pygame.Vector2(x, y)

vec.magnitude()
vec.normalize()
vec.angle_to(another_vec)
```

> Pygame rect

```python
rect = pygame.Rect(x, y, width, height)

rect.x # int
rect.y # int
rect.center # [int, int]
rect.centerx # int
rect.centery # int

rect.colliderect(another_rect) # bool
rect.collidepoint(x, y) # bool
```

> Pygame Draw primitive shapes

```python
pygame.draw.circle(surface, color, center, radius)
pygame.draw.rect(surface, color, [x, y, width, height])
pygame.draw.rect(surface, color, rect)
pygame.draw.line(surface, color, (x1, y1), (x2, y2), thickness)
```

> Pygame basic functions

```python
import pygame # imports pygame library

window = pygame.display.set_mode([width, height]) # creates a window surface
clock = pygame.time.Clock() # creates a clock that controls the event loop

clock.tick() # gives delta time in milli seconds
pygame.display.update() # updates the frame
surface.fill(color) # fills the surface with a given color

pygame.event.get() # gives an array of events that have been triggered in that particular frame
```

## Questions

> 1. Implement a ray casting system where you have to check if there is an enemy
in the line of sight of player when he shoots. If there are enemies in the line of sight
call the enemy's reset() method

> 2. Implement the enemies movement code where the enemies move
towards the player always

> 3. Implement the enemies movement code where the enemies move
towards the player only when the player is in the line of sight of the
enemy
