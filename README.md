# Mutable Resume Portfolio
Have you ever wanted to apply with a tailored resume, but found the process of editing, updating, and managing different resumes, frusterating?

Most resume generators focus on making one good resume. Anything more than that usually costs money in the form of a subscription. This is inconvenient for you as a job seeker because
1. Your resume changes over time
2. You need a way to manage multiple resumes to maximize their odds of standing out amoungst hundreds of applicants. i.e, you need a way *modularize* different skillsets to showcase for different positions
3. Sometimes downloading a file isn't the most convenient form. A lot of networking is done informally via links. Having more control over your own data isn't just better for your wallet, but helps make it easy to self host your resumes and share them (which this app is designed for)
4. You need something free to use. You are looking for a job, not trying to spend more money


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

## Claude/GPT/DeepSeek Prompt for generating recommendations
The following is a job description for a position I am applying to:
```md

```
Please generate:
1. a few ideas for what would generally be effective on a resume for this job
2. concise list of key college courses in my education section
3. list of 15 MAX key technical skills (like languages, frameworks, etc. but do not categorize them) in my skills section
4. list of 10 MAX key conceptual skills (like paradigms, types of work for this tech role, etc.) in my skills section 
5. concise list of projects to highlight in my projects section

## Useful resources
- https://www.reddit.com/r/EngineeringResumes/wiki/index/?share_id=JPpfQ581Ep7v7Hk6Gl3pd&utm_content=1&utm_medium=ios_app&utm_name=ioscss&utm_source=share&utm_term=1#wiki_disclaimer.3A_your_submission_will_get_taken_down_if_you_do_not_read_this_wiki.
- https://thetechresume.com/samples/ats-myths-busted

## Crafting experiences section:
Each bullet point should follow STAR, XYZ, or CAR
STAR: Situation, Task, Action, and Results

https://www.levels.fyi/blog/applying-star-method-resumes.html
https://resumegenius.com/blog/resume-help/star-method-resume
XYZ: Accomplished [X] as measured by [Y], by doing [Z]

https://www.inc.com/bill-murphy-jr/google-recruiters-say-these-5-resume-tips-including-x-y-z-formula-will-improve-your-odds-of-getting-hired-at-google.html
https://elevenrecruiting.com/create-an-effective-resume-xyz-resume-format/
CAR: Challenge Action Result

https://ca.indeed.com/career-advice/resumes-cover-letters/challenge-action-result-resume
https://www.topresume.com/career-advice/how-to-get-more-results-with-a-car-resume

If you're able to quantify your achievements/results, move the metrics towards the start of each bullet

# TODO:
- errors
- colons

- icon height
- colons
- remove bolds
- fix project hyphen