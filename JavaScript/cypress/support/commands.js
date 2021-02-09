// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add("login", (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add("drag", { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add("dismiss", { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite("visit", (originalFn, url, options) => { ... })

Cypress.Commands.add("acceptCookies", () => {
    cy.setCookie('OptanonAlertBoxClosed', new Date().toISOString())
})

Cypress.Commands.add("stubSearchResults", (city) => {
    cy.intercept(`/get-involved/find-a-shop?field_shop_geocode_latlon=${city}&items_per_page=10`, 
    { fixture: 'tbody.html' })
})
