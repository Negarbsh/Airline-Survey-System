//
//  ManagerLoginView.swift
//  AirLineSurveys
//
//  Created by Amirhossein Razlighi on 10/01/2023.
//

import SwiftUI

struct ManagerLoginView: View {
    @State private var username = ""
    @State private var password = ""
    @State private var goToNextView = false
    @State private var wrongCredentials = false
    @State private var scaleRadOuter : CGFloat = 1.7

    
    
    var body: some View {
        let scaleRadInner : CGFloat = 1.35
        
        var authManager = AuthManager(isManager: true, username: username, password: password)
        
            ZStack {
                
                Color.blue
                    .ignoresSafeArea()
                
                Circle()
                    .scale(scaleRadOuter)
                    .foregroundColor(.white.opacity(0.2))
                    .animation(.easeInOut(duration: 3).repeatForever(autoreverses: true), value: scaleRadOuter)
                    .onAppear {
                        scaleRadOuter = 1.7
                        scaleRadOuter += 0.1
                    }

                Circle()
                    .scale(scaleRadInner)
                    .foregroundColor(.white)

                
                VStack {
                    Text("Login For Managers:")
                        .font(.largeTitle)
                        .bold()
                        .padding()
                    
                    TextField("username", text: $username)
                        .padding()
                        .frame(width: 300, height: 50)
                        .background(Color.black.opacity(0.05))
                        .cornerRadius(5)
                        .border(.red, width: wrongCredentials ? 1 : 0)
                    
                    TextField("password", text: $password)
                        .padding()
                        .frame(width: 300, height: 50)
                        .background(Color.black.opacity(0.05))
                        .cornerRadius(5)
                        .border(.red, width: wrongCredentials ? 1 : 0)
        
                        
                    NavigationLink(destination: EmptyView(), isActive: $goToNextView) {
                        Button("Login!") {
                            goToNextView = true
                            wrongCredentials = authManager.main()
                        }
                        .foregroundColor(.white)
                        .frame(width: 300, height: 50)
                        .background(.blue)
                        .cornerRadius(10)
                    }
                    }
            }
    }
}


struct ManagerLoginView_Previews: PreviewProvider {
    static var previews: some View {
        ManagerLoginView()
    }
}
