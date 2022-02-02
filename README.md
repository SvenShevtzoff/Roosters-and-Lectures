
# Lectures & Lesroosters

In this case, we are trying to generate a schedule for a school or university. Three data files were provided by the course. The data we have is:

- courses.csv, a file containing all courses to be scheduled. In this file information on each course is contained: the number of lectures, tutorials and practica, the maximum number of students in tutorials and practica and the expected number of students;
- rooms.csv, a file containing the seven rooms we can use and their maximum capacity;
- students_and_courses.csv, a file containing 609 students and the courses they enrolled for.

Generating a schedule means putting every activity (which is a lecture, tutorial or practicum) in a so-called 'roomslot': this is a combination of a room and a timeslot. For example, Monday from 09:00 to 11:00 in room C0.110. 

It is known that there is no perfect solution to this problem. Our goal is to find a solution that is as good as possible. We measure 'as good as possible' by counting 'malus points': the less malus points, the better the schedule. We get malus points for the following things:

- a student has a gap hour (one malus point);
- a student has two gap hours (three malus points);
- a student has conflicts in their schedule (for example, two activities in the same timeslot) (one malus point);
- using the evening timeslot (17:00 - 19:00) (five malus points);
- one malus point for every student that does not fit in a room.

In certain cases, the schedule is illegal and should be rejected. That is when any student has three gap hours or more students are in a tutorial/practicum than the maximum amount of students allowed in that activity. Considering this malus points system, an important part of this project was writing a correct 'fitness function' that calculates the number of malus points, given a schedule.


## Authors

- [Sven Shevtzoff (12290513)](https://github.com/SvenShevtzoff) 
- [Vera Duindam (12146307)](https://github.com/veraduindam) 
- [Marc Vlasblom (14078163)](https://github.com/marcBook-air)


## Data structure

For an overview of the data structure please refer to the [ClassesUML file](https://github.com/SvenShevtzoff/Roosters-and-Lectures/blob/main/doc/classesUML.png) in the doc folder.


## Algorithms

We wrote four different algorithms which can be used to generate a schedule:

- randomise (constructive): this algorithm links every activity to a random roomslot;
- greedy (constructive): this algorithm sorts the activities (activities with the most enrolled students first) and roomslots (rooms with greatest capacity first) and then links them in this sorted order. This way, activities with the most students get set to the roomslots with the largest room;
- hillclimber (iterative): this algorithm starts by generating a random schedule, then makes some mutations to this schedule (moving a student to another tutorial/practicum group or moving/swapping an activity to another roomslot) and then checks if there are less malus points. If so, keep this new schedule, if not, go back to the old schedule;
- genetic (iterative): generate N random schedules, take M schedules with the least amount of malus points, and combine these to create new schedules('reproducing').

It appears that it is very hard to create a 'legal' schedule (a schedule without any three gap hours and not maximums in activities exceeded) with our constructive algorithms. This is because of the large number of students. That is why we combined `randomise` and `greedy` with `hillclimber`. In the algorithms `randomise_baseline` and `greedy_baseline`, we create random and greedy schedules and then change them using a hillclimber algorithm until they are legal.
In the iterative algorithms, constraint relaxation is used. This means that the start state does not have to be valid, but a lot of malus points are given in case of an invalid schedule. That is, 1000 malus points for every student with 3 gap hours and 1000 malus points for every activity where the maximum is exceeded.


## Usage

When running this program, a schedule is generated using one of our algorithms, and the number of malus points of this schedule is printed.

Before the program can be excecuted make sure to install the right packages using the following:

    pip3 install -r requirements.txt

To run the program, the following command can be used

    python3 main.py [algorithm_name]
    algorithm options: ["randomise", "randomise_baseline", "greedy", "greedy_baseline", "hillclimber", "genetic"]

When no algorithm is specified this list of possibilities is printed.


## Output

For the output a seperate folder is specified, all files in this folder will be ignored by the repository, but the folder is used by the algorithms. At the bottom of the main, some example schedules will be visualized and the best schedule is outputted to csv, this can be changed there. Also the method 'visualize_rooms()' is called on the best_schedule. This creates 7 schedule visualizations of the 7 rooms to get an overview of the entire schedule.
