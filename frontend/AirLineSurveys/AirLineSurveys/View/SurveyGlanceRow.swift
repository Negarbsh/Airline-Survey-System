//
//  SurveyGlanceRow.swift
//  AirLineSurveys
//
//  Created by Amirhossein Razlighi on 10/01/2023.
//

import SwiftUI

struct SurveyGlanceRow: View {
    var surveyInfo: SurveyInfo = SurveyInfo(id: 1, activationInterval: Date(), isActive: false, relatedAirlineId: 2, isTaken: false)
    
    var body: some View {
        
        HStack {
                    VStack(alignment: .leading) {
                        Text(surveyInfo.isActive ? "Active" : "InActive")
                            .font(.custom("Futura-Medium", size: 10, relativeTo: .subheadline))
                            .padding(.horizontal, 2)
                        Image(systemName: surveyInfo.isActive ? "checkmark" : "multiply")
                            .foregroundColor(surveyInfo.isActive ? .green : .red)
                            .padding(.horizontal, 10)
                    }
                    .frame(width: 41.0, alignment: .leading)
                    Divider()
                    VStack(alignment: .leading) {
                        Text(surveyInfo.activationInterval, style: .date)
                            .font(.custom("Futura-Medium", size: 20.0, relativeTo: .title3))
                        Text("Due Date")
                            .font(.caption2)
                            .fontWeight(.semibold)
                            .foregroundColor(.gray)
                    }
                    .padding(.leading, 8.0)
                    Spacer()
                    Image(systemName: "airplane")
                        .resizable()
                        .scaledToFit()
                        .frame(width: 20.0)
                        .foregroundColor(.blue)
                    Spacer()
                    VStack(alignment: .trailing) {
                        Text(surveyInfo.isTaken ? "Completed" : "Take Survey")
                            .font(.caption2)
                            .foregroundColor(surveyInfo.isTaken ? .green : .red)
                    }
                }
                .frame(maxWidth: .infinity)
                .padding(.vertical, 8.0)
            }
    }

struct SurveyGlanceRow_Previews: PreviewProvider {
    static var previews: some View {
        SurveyGlanceRow()
            .frame(height: 80)
            .padding(.horizontal)
            .previewLayout(.sizeThatFits)
    }
}
