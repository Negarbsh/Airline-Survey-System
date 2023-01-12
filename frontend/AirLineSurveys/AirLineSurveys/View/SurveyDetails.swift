//
//  SurveyDetails.swift
//  AirLineSurveys
//
//  Created by Amirhossein Razlighi on 10/01/2023.
//

import SwiftUI

struct SurveyDetails: View {
    @StateObject var questions: Question = Question(id: 1, questionNumber: 1, questionText: "SALAM")
    
    var body: some View {
        NavigationView {
            ScrollView {
                ZStack {
                    Color.green
                    VStack {
                        Text("Hello")
                    }
                }
                .frame(height: 30)
            }
        }
    }
}

struct SurveyDetails_Previews: PreviewProvider {
    static var previews: some View {
        SurveyDetails()
    }
}
