import QtQuick
import QtQuick.Controls.Material
import "../Components"

Paper {
    id: paper
    height: parent.height
    width: 84

    signal navigateToPage(var page)

    Column {
        id: column
        width: parent.width
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        spacing: 4
        topPadding: 4
        bottomPadding: 4

        IconButton {
            anchors.horizontalCenter: parent.horizontalCenter
            implicitHeight: parent.width / 2 + 20
            implicitWidth: parent.width / 2 + 20
            iconSource: "../../resources/icons/home.svg"
            iconSize: 32
            onClicked: paper.navigateToPage("../ui/pages/Home.qml")
        }

        IconButton {
            anchors.horizontalCenter: parent.horizontalCenter
            implicitHeight: parent.width / 2 + 20
            implicitWidth: parent.width / 2 + 20
            iconSource: "../../resources/icons/home.svg"
            iconSize: 32
            onClicked: paper.navigateToPage("../ui/pages/ManageAntenna.qml")
        }
    }
}
