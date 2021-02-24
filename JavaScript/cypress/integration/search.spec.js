/// <reference types="cypress" />

describe('Search', () => {
    // Task 3: Refactor beforeEach...
    beforeEach(() => {
        cy.acceptCookies()
        cy.visit('/')
        cy.get('.links').children('li').first('a').click()
        cy.get('#main-content').children('h1').should('have.text', 'Shop search results')
    })

    // Task 1: finish this test
    it('happy scenario', () => {
        cy.get('.breadcrumb').invoke('text')
            .should('contain', 'Shop search results')
            .and('contain', 'Get involved')
            .and('contain', 'Home')

        cy.url().then((url) => {
            cy.visit(`${url}?field_shop_geocode_latlon=london&items_per_page=10`)
        })

        cy.fixture('shop').then((shop) => {
            cy.contains(shop.postCode)
        })
    })

    // Task 2: Unskip and finish this test
    it.skip('negative scenario', () => {
    })
})
