Salesforce Test Automation

# Introduction

This repository is a test automation framework using Playwright with CucumberJS written in Typescript. It also uses the Javascript library JSforce for API interaction with Salesforce.

- [Playwright Documentation](https://playwright.dev/)
- [Cucumber Documentation](https://cucumber.io/docs/guides/overview/)
- [Typescript Documentation](https://www.typescriptlang.org/)
- [JSforce Documentation](https://jsforce.github.io/)

# Getting Started

It is recommended to use [Visual Studio Code (VSCode)](https://code.visualstudio.com/download) to modify the framework.
The following extensions will make it easier to develop the tests and framework:

- [Playwright Test for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-playwright.playwright)
- [Cucumber for VSCode](https://marketplace.visualstudio.com/items?itemName=CucumberOpen.cucumber-official)

## Setting up the Test Repository

Install the following pre-requisites on your machine

1. [NodeJS](https://nodejs.org/en)

In a terminal window, type the following where you want to setup the repository

1. Clone this repository to your local machine

2. Once inside the root directory of the project, initialise and install all the dependencies:

   `npm install`

3. Install the Playwright browsers:

   `npx playwright install`

## Setting .env

To run the tests, you need to create a [Salesforce Developer Edition](#sign-up-for-salesforce-developer-edition) sandbox.  
You'll find the template .env.template file in the root of the repository. Copy this and save it as `.env` in the root directory of the repo. Update the variables with your Salesforce Developer Edition information.

**Note:** Do not put a forward slash at the end of SALESFORCE_URL ([Explanation](/documentation/issues.md#goto-not-going-to-expected-location))

```
SALESFORCE_URL=
SALESFORCE_USERNAME=
SALESFORCE_PASSWORD=
SALESFORCE_SECURITY_TOKEN=
```

**Warning:** Do not commit this file

## Running the tests

Run all the tests in headless mode with `npm test`.

Run all the tests in headed mode with `npm run test:headed`.

To run select tests in headed mode, add `@debug` to those features and/or scenarios and run with `npm run test:debug`.

### Running unit tests

Run all the unit tests with `npm run test:unit`.

# Sign Up For Salesforce Developer Edition

You will be required to sign up for a Salesforce Developer Edition account to run the framework against when running locally.  
Complete the form at [developer.salesforce.com](https://developer.salesforce.com/signup) to get your free sandbox environment.  
You will need to enter your developer account URL, username, and password into the .env file. Instructions found [here](#setting-env).

## Reset Security Token

When you use JSforce to access the Salesforce API, you need a security token to login. Follow the instructions below to generate your security token.

1. In the browser, log in to your Developer org with your user's credentials.
2. Click on your avatar in the top right corner to view profile drop down.
3. Select `Settings` to direct to your personal settings.
4. On the navigation bar to the left, click `Reset My Security Token` under My Personal Information.
5. Click the `Reset Security Token` button.
6. The security token will be sent to the email address you used to set up your Salesforce Developer Edition account.

You will need to enter your Security Token into the .env file. Instructions found [here](#setting-env).

# Documentation

- [Documentation](/documentation/documentation.md)
- [GitHub Actions](/documentation/github-workflows.md)
- [Playwright Locator Generator Helper](/documentation/locator-generator-helper.md)
- [Issues](/documentation/issues.md)
