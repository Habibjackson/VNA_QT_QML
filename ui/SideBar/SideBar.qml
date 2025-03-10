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
            id: manageAntennaBtn
            anchors.horizontalCenter: parent.horizontalCenter
            implicitHeight: parent.width / 2 + 20
            implicitWidth: parent.width / 2 + 20
            iconSource: "../../resources/icons/ManageAntenna.svg"
            iconSize: 32
            onClicked: paper.navigateToPage("../ui/pages/ManageAntenna.qml")
            CTooltip {
                text: qsTr("Manage Antenna")
                visible: manageAntennaBtn.hovered
                target: manageAntennaBtn
            }
        }

        IconButton {
            id: testsBtn
            anchors.horizontalCenter: parent.horizontalCenter
            implicitHeight: parent.width / 2 + 20
            implicitWidth: parent.width / 2 + 20
            iconSource: "../../resources/icons/TestIcon.svg"
            iconSize: 32
            onClicked: paper.navigateToPage("../ui/pages/Tests.qml")
            CTooltip {
                text: qsTr("Tests")
                visible: testsBtn.hovered
                target: testsBtn
            }
        }

        IconButton {
            id: toolsBtn
            anchors.horizontalCenter: parent.horizontalCenter
            implicitHeight: parent.width / 2 + 20
            implicitWidth: parent.width / 2 + 20
            iconSource: "../../resources/icons/tools.svg"
            iconSize: 32
            onClicked: paper.navigateToPage("../ui/pages/Tools.qml")
            CTooltip {
                text: qsTr("Tools")
                visible: toolsBtn.hovered
                target: toolsBtn
            }
        }
    }
}
