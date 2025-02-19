# News

## 2022-03-19 — No GUI Update, focus on CLI improvements

After some pondering, I've decided to shelve the actual GUI update and instead continue working on the CLI python version.

There were a lot of reasons against a GUI update.
But mainly, it would require a lot of time and energy to do a GUI and rewrite the entire application.
I'd rather spend time fixing existing bugs, improving the CLI and installation process, and making it more user-friendly.

### Pros of shelving GUI

- Would take 1+ years to catch up to the python version in functionality.
- More energy and time to actually make a fantastic CLI version
- CurseForge already has a good and easy-to-use GUI for updating mods.
- Less competition with CurseForge

### Cons of shelving GUI

- No mod manager can download from either CurseForge or Modrinth with GUI support;
  but hopefully someone else will create one? :)
- Less accessible to ordinary people that don't have experiences with CLIs

### Who will use mcman?

With that said, I'm thinking of doubling down on the CLI and making it excellent.
mcman is for technical people and server managers who want an automatic way to update the mods.
Of course, ordinary people can still use it, but the main focus will be to cater to the former's needs.

### Future releases

Now to the fun part, what's to come in the subsequent releases.

#### v1.3 – Installation improvements

The main plan is to improve the installation process.
There are a few mods that can't be found, even though they clearly exist on CurseForge.
I have a solid plan for solving this issue, but only half the problems will be solved in v1.3.
The rest will be implemented in v1.4, which focuses on User Experience (UX)

Automatically installing dependencies will also come in this release :tada:

This release will also focus on fixing a lot of bug fixes.

[see issues linked to v1.3](https://github.com/Senth/minecraft-mod-manager/milestone/4)

#### v1.4 – User Experience (UX)

The main plan here is to focus on improving accessibility.
Asking for user input when mcman doesn't know how to handle the situation.
Making the CLI consistent, and maybe even changing it up a bit.

[see issues linked to v1.4](https://github.com/Senth/minecraft-mod-manager/milestone/5)

### Thank You!

As the last message, I want to thank everyone who contributes to this project.
Through ideas, through bug reports, and just by using it :slight_smile:

Thank you!
/ Senth

## 2022-01-27 — The GUI Update (late 2022)

There was an idea of adding a GUI to python.
Unfortunately, python development is not meant for fast GUI development.
So testing changes often requires restarting the application,
this is less than ideal especially when I'm used to changing the code and seeing updates directly.

It's one of the reasons the progress stopped on this because it was slow and frustrating.

Thus I started looking for alternatives and found [Electron](https://www.electronjs.org/) to hopefully be a good fit.
This way I can leverage my existing web development skills for creating an GUI instead of learning another.
I still want to support a CLI though, but I think this can be done even on servers. It's a main requirement.
Of course the new App will be cross platform.

What this means is that I'll start "scratch". But I'd almost have to do that either way with the changes I wanted to do.

## 2021-09-10 — The GUI Update (early 2022)

I'm currently working on a GUI update that simplifies the use of `mcman`.
I'm planning to be done with it early 2022.
At first, I wanted to be done before Minecraft 1.18 releases, but after creating most issues, I doubt that will be the case.

You can find more detailed information in [#38](https://github.com/Senth/minecraft-mod-manager/issues/38).
Or check out [the project](https://github.com/Senth/minecraft-mod-manager/projects/1)
to check the progress and upcoming tasks
