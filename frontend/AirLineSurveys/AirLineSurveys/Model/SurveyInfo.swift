//
//  SurveyInfo.swift
//  AirLineSurveys
//
//  Created by Amirhossein Razlighi on 10/01/2023.
//

import Foundation

struct SurveyInfo: Codable, Identifiable {
    var id: Int
    var activationInterval: Date
    var isActive: Bool
    var relatedAirlineId: Int
    var isTaken: Bool
    
    var stringFormattedDate: String {
        let dateFormatter = DateFormatter()

        return dateFormatter.string(from: self.activationInterval)
    }

}
