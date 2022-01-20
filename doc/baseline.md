# Baseline

For the baseline, we ran an algorithm that produces a random schedule. We created lectures, practica and tutorials (in a general class called `Activity`) for each course, adjusted to the amount of students that signed up for the course. Then, we chose a random roomslot for each activity. We ran the code 10000 times, calculating the number of malus points at every run. The results can be seen below.


## Bias

The way we calculate the number of tutorials/practica needed now is by dividing the number of enrolled students by the maximum amount of students allowed in a tutorial/practicum, and then ceiling that number. For example, if there are 27 students enrolled and the tutorial has a maximum of ten students, we create three tutorials. However, more tutorials/practica than the minimum is also an element of the state space. 