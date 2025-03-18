import QtQuick 6.5
import QtQuick.Controls 6.5
import QtQuick.Layouts
import "BottomBar"
import "SideBar"
import "Components"

Window {
    property var theme: Theme {}
    readonly property double margin: 12

    visible: true
    width: settingsManager.windowWidth
    height: settingsManger.windowHeight
    id: applicationWindow
    title: "VNA Automation"
    minimumWidth: 400
    minimumHeight: 500

    color: theme.backgroundColor

    RowLayout {
        spacing: applicationWindow.margin
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: bottomBar.top
        anchors.margins: applicationWindow.margin

        SideBar {
            id: sideBar
            Layout.fillHeight: true
            onNavigateToPage: page => pageContent.mainStack.push(page)
        }

        MainContent {
            id: pageContent
            Layout.fillHeight: true
            Layout.fillWidth: true
            clip: true
            // width: parent.width - sideBar.width
        }
    }

    BottomBar {
        id: bottomBar
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: parent.right
    }
}
