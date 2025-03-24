import QtQuick 6.5
import QtQuick.Controls 6.5

ApplicationWindow {
    id: splashWindow
    visible: true
    width: 800
    height: 600
    color: "#2E2E2E"

    Rectangle {
        id: splashBackground
        anchors.fill: parent
        color: "#1E1E1E"

        // Image {
        //     id: logo
        //     source: "qrc:/images/logo.png"
        //     anchors.horizontalCenter: parent.horizontalCenter
        //     anchors.verticalCenter: parent.verticalCenter
        //     width: 200
        //     height: 200
        //     fillMode: Image.PreserveAspectFit
        // }
        BusyIndicator {
            id: loadingIndicator
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.top: logo.bottom
            anchors.topMargin: 20
            running: true
        }
    }

    Timer {
        interval: 3000 // 3 seconds
        running: true
        repeat: false
        onTriggered: {
            // Emit signal to load main application
            mainAppLoader.source = "../main.qml"
        }
    }

    Loader {
        id: mainAppLoader
    }
}
