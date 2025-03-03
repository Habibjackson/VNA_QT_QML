import QtQuick 6.5
import QtQuick.Controls 6.5
import "BottomBar"
import "SideBar"
import "Components"

Window {
    property var theme: Theme {}
    readonly property double margin: 12

    visible: true
    width: 1280
    height: 720
    id: applicationWindow
    title: "VNA Automation"

    color: theme.backgroundColor

    SideBar {
        id: sideBar
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.bottom: bottomBar.top
        onNavigateToPage: page => pageContent.mainStack.push(page)
        anchors.margins: applicationWindow.margin
    }

    MainContent {
        id: pageContent
        anchors.left: sideBar.right
        anchors.bottom: bottomBar.top
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.margins: applicationWindow.margin
        clip: true
        // width: parent.width - sideBar.width
    }

    BottomBar {
        id: bottomBar
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: parent.right
    }
}
