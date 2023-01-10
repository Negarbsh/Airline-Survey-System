//
//  SurveyRow.swift
//  AirLineSurveys
//
//  Created by Amirhossein Razlighi on 10/01/2023.
//

import SwiftUI

struct SurveyList: View {
    @State private var surveyInfos : [SurveyInfo] = [SurveyInfo(id: 1, activationInterval: Date(), isActive: true, relatedAirlineId: 1, isTaken: false), SurveyInfo(id: 2, activationInterval: Date().advanced(by: 2 * 24 * 60 * 60), isActive: false, relatedAirlineId: 1, isTaken: true)]
    
    var body: some View {

        NavigationView {
                VStack {
                    Image("Ukraine_Airlines")
                        .resizable()
                        .scaledToFit()
                        .frame(maxWidth: .infinity,maxHeight: 150)
                    
                    List {
                        Section {
                            ForEach(surveyInfos) { surveyInfo in
                                NavigationLink(destination: EmptyView()) {
                                    SurveyGlanceRow(surveyInfo: surveyInfo)
                                }
                            }
                        }
                    }
                    .navigationTitle("surveys at a glance!")
                }
        }
        .ignoresSafeArea()
    }
}

struct SurveyList_Previews: PreviewProvider {
    static var previews: some View {
        SurveyList()
    }
}
