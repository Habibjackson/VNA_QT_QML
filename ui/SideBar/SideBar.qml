import QtQuick
import QtQuick.Controls.Material
import "../Components"

Paper {
    id: paper
    height: parent.height
    width: 64

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
            iconSource: "../../resources/icons/tests.svg"
            iconSize: 32
            onClicked: paper.navigateToPage("../ui/pages/ManageAntenna.qml")
        }

        IconButton {
            anchors.horizontalCenter: parent.horizontalCenter
            implicitHeight: parent.width / 2 + 20
            implicitWidth: parent.width / 2 + 20
            iconSource: "../../resources/icons/tools.svg"
            iconSize: 32
            onClicked: paper.navigateToPage("../ui/pages/ManageAntenna.qml")
        }
    }
}
