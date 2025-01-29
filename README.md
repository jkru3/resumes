# Resume Generator
Have you ever wanted to apply with a tailored resume, but found it frusterating to put in the effort for it?

Spinning up new custom tailored resumes fast, free, and easy. With just a VScode extension, you can writeup all your experiences as LaTeX modules and then make as many templates as you want, drag and dropping modules like legos to fit the needs of the job you are applying for. The best part? It's easy to save, store, and build upon all the templates you use as you improve it.

## Requirements
python 3.8+
run `brew install texlive`
install the 'LaTeX workshop' VScode extension

## Usage
Create resume templates and then save them. With LaTeX workshop, they are automatically compiled into PDFs

Deploying this through GitHub pages will allow you to refer to any of the PDFs in the ./build directory as a link, so anyone you want to share a tailored resume with can see it!

# Resume tips:
Follow the form
1. Accomplished X
2. Measured by Y
3. By doing Z

## Claude/GPT/DeepSeek Prompt for generating ATS recommendations
The following is a job description for a position I am applying to:
```md

```
Please generate:
1. generally what would be effective on a resume for this job
2. string-array list of college courses that would be good to include on a resume
3. string-array list of technical skills (languages, frameworks)
4. string array list of conceptual skills (paradigms, types of work for this tech role)
5. string-array list of types of projects to include in my projects section