//
//  AuthenticationManager.swift
//  AirLineSurveys
//
//  Created by Amirhossein Razlighi on 10/01/2023.
//

import Foundation


struct AuthManager {
    var isManager: Bool
    var username: String
    var password: String
    
    func main() -> Bool {
        if (self.isManager) {
            //TODO: send username and password for manager login
            return false
        } else {
            //TODO: send flightNumber and TicketNumber for voter login
            return true
        }
    }
}
