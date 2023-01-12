//
//  DescriptiveQuestion.swift
//  AirLineSurveys
//
//  Created by Amirhossein Razlighi on 10/01/2023.
//

import Foundation


class DescriptiveQuestion: Question {
    var answer: String
    
    init(id: Int, questionNumber: Int, questionText: String, answer: String) {
        self.answer = answer
        super.init(id: id, questionNumber: questionNumber, questionText: questionText)
    }
}
