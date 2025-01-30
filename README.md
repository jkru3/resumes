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
1. a few ideas for what would generally be effective on a resume for this job
2. concise list of key college courses in my education section
3. list of 15 MAX key technical skills (like languages, frameworks, etc. but do not categorize them) in my skills section
4. list of 10 MAX key conceptual skills (like paradigms, types of work for this tech role, etc.) in my skills section 
5. concise list of projects to highlight in my projects section