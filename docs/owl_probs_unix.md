# The Owl, Problem Solving, and the Unix Workbench

![Image of circles and owl](../static/owl.jpg)

Why does programming feel hard, especially when first learning the basics?

One major source of frustration is the sheer range of skills and tools you may be trying to learn at once:

* Code editing tool
* Programming language(s)
* Tools surrounding the language such as third-party libraries, package installers, etc.
* Version control

The list goes on (and on). And let's not forget the actual task at hand, which likely involves acquiring, wrangling, analyzing and visualizing data.

So how do we cut through the stress and get things done?

## Cut your problems down to size

> *"If you can't solve a problem, then there is an easier problem you can solve: find it." ~ George Pólya*

Below is a smattering of advice for the budding programmer. Hopefully, these tidbits will help you approach new projects with a greater sense of calm, and equip you to power through the inevitable roadblocks.

**Don’t have one big problem.** *Choose* to have numerous small problems. If the goal is to analyze election results, spend some time creating a high-level roadmap for the project. Ask yourself -- what data sources will I need and where I will I get them? Do I need to write a scraper? If so, which scraping library is most suited to the task? What analyses are important to conduct? What are my finished outputs (story narrative, a map, etc.)? 

You can apply this methodology to varying degrees of granularity. Just try to keep it high-level and avoid the rabbit hole of over-planning.

**Talk it out.** Talking to a friend, colleague or even a [rubber duck][] can help identify strategies and tools, prioritize tasks, and map out a clear path forward.

[rubber duck]: https://en.wikipedia.org/wiki/Rubber_duck_debugging

**Whiteboard it.** There's a reason whiteboards have become synonymous with start-up culture. They allow you to externalize thoughts and encourage collaborative problem-solving. If you don't have a whiteboard, never fear. Dead trees also work. The crucial thing is to get the ideas out of your head, identify potential roadblocks and complexities, and draft a plan of attack.

**Read the docs.** When using a new tool or library, don't just head to StackOverflow to copy/paste a "solution". Spend a few minutes skimming the official documentation and getting a sense of the library's features. Walk through the tutorial. Then try writing your own code. You'll gain a more intuitive sense of what each line of your code does, how to find answers in the official documenations, and develop ambient awareness of the library's full set of features.

**Tinker, Build (rinse and repeat).** Rather than immediately writing the code for a project, take some time to experiment with the various libraries required for the project. If you're scraping data, fire up an interactive Python shell or write a "toy" Python script that scrapes data from a simple web page. Then try adapting your experiments to that government website you're itching to scrape. Tinkering on simple use cases will help build confidence and familiarity with libraries, and prepare you to adapt them to more advanced use cases.

**Add tools gradually.** The ecosystem of languages, tools and libraries involved in programming can easily overwhelm new programmers (as well as veterans). You'll no doubt come across highly opinionated folks advocating a particular set of tools or workflows. Don't feel you need to adopt their opinions! Start simple. You only need a text editor, the Bash shell, and a general purpose programming language like Python to get started. As you gain experience, add tools and language features as the opportunities arise.

**There is no final state of mastery**. Programming is a journey, not a destination. Even the most experienced coders don't "know it all". Release yourself from the expectation that you will magically arrive at a place where you've mastered a language or tool. Plan on forgetting syntax and features, even after using them hundreds or thousands of times. That's why we have docs :)

![xkcd tar forgetting](https://imgs.xkcd.com/comics/tar.png)

## Problem solving, the Unix way

> *"Every woodworker needs a good, solid, reliable workbench, somewhere to hold work pieces at a convenient height while he or she works them...For a programmer manipulating files of text, that workbench is the command shell." ~ The Pragmatic Programmer, p. 77*

Pólya's advice on problem-solving works nicely in tandem with Unix
tools, which are inspired by the more general [Unix
Philosophy](https://en.wikipedia.org/wiki/Unix_philosophy) of 
"Do One Thing and Do It Well."

Before diving into solving a big Problem (with a capital "P"), take time to break it down into smaller parts. Externalize your strategy on paper or whiteboard until you have a discrete set of problems.

Then, search for Unix tools or features that can solve each problem. As you identify tools, don’t immediately dive into implementing your
solution. Take some to read about and experiment with each tool.
Gradually build up your solution to each sub-problem. Along the way, don't forget that you can use [Unix pipes and filters][] to create multi-step pipelines:

```
$ cat animals.txt | head -n 5 | tail -n 3 | sort -r > final.txt
```

[Unix pipes and filters]: https://swcarpentry.github.io/shell-novice/04-pipefilter/index.html

Finally, combine your "sub-solutions" into a single script -- or perhaps several -- that can be run on demand.

## Recommended Reading

* [The Pragmatic Programmer, Shell Games (Section 15)](https://searchworks.stanford.edu/view/8257021)
* [How to Solve It](https://en.wikipedia.org/wiki/How_to_Solve_It)
* [Unix Philosophy](https://en.wikipedia.org/wiki/Unix_philosophy)

## Technical Resources

* [CLI cheat sheet](https://www.git-tower.com/blog/command-line-cheat-sheet/)
* [Explain Shell](https://explainshell.com/)
* [The Unix Shell](http://swcarpentry.github.io/swc-releases/2017.08/shell-novice/)
