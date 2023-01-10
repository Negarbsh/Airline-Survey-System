//
//  ContentView.swift
//  AirLineSurveys
//
//  Created by Amirhossein Razlighi on 10/01/2023.
//

import SwiftUI

struct ContentView: View {
    @State private var showManagerLogin = false
    @State private var showPassengerLogin = false
    
    var body: some View {
        NavigationView {
            ZStack {
                Color.pink
                    .ignoresSafeArea()
                Circle()
                    .scale(1.7)
                    .foregroundColor(.white.opacity(0.15))
                Circle()
                    .scale(1.35)
                    .foregroundColor(.white)
                
                VStack {
                    Text ("Welcome to Airline Surveys\' System")
                        .font(.largeTitle)
                        .padding()
                    
                    NavigationLink(destination: ManagerLoginView(), isActive: $showManagerLogin) {
                        Button("I'm a manager") {
                            showManagerLogin = true
                        }
                        .foregroundColor(.white)
                        .frame(width: 320, height: 50)
                        .background(.blue)
                        .cornerRadius(10)
                        .padding(.top)
                    }

                    NavigationLink(destination: VoterLoginView(), isActive: $showPassengerLogin) {
                        Button("I'm a Passenger") {
                            showPassengerLogin = true
                        }
                            .foregroundColor(.white)
                            .frame(width: 320, height: 50)
                            .background(.red)
                            .cornerRadius(10)
                        .padding(.bottom)
                    }
                }
            }
        }
        .accentColor(.white)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
