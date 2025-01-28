# Resume Generator
Ever wanted to apply with a tailored resume, but tired of how long it takes?

Wouldn't it be nice to have a record of every resume you have ever made?

Spinning up new custom tailored resumes fast, free, and easy. With this simple python application, you can writeup all your experience as LaTeX modules and then make as many templates as you want, drag and dropping modules like legos to fit the needs of the job you are applying for. The best part? It's easy to save, store, and build upon all the templates you use as you improve it.

## Requirements
python 3.8+
LaTeX workshop
- Set `"latex-workshop.latex.outDir": "../build"` to keep pdfs separate from templates
- Run `Latex Workshop: Clean up auxiliary files` using `shift + cmd + P` in VS Code with a mac to remove the auxilary files before pushing to a website like github

## Usage
Create resume templates and then save them. With LaTeX workshop, they are automatically compiled into PDFs

Deploying this through GitHub pages will allow you to refer to any of the PDFs in the ./build directory as a link, so anyone you want to share a tailored resume with can see it!