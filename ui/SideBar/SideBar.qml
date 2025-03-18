import QtQuick
import QtQuick.Controls.Material
import QtQuick.Layouts
import "../Components"

Paper {
    id: paper
    height: parent.height
    width: 64

    signal navigateToPage(var page)

    Column {
        id: column
        width: parent.width
        height: parent.height
        // spacing: 8

        RoundButton {
            id: manageAntennaBtn
            radius: 4
            anchors.horizontalCenter: parent.horizontalCenter
            Layout.fillHeight: false
            implicitHeight: parent.width / 2 + 20
            implicitWidth: parent.width / 2 + 20
            icon.source: "../../resources/icons/ManageAntenna.svg"
            // iconSize: 32
            onClicked: paper.navigateToPage("../ui/pages/ManageAntenna.qml")
            CTooltip {
                text: qsTr("Manage Antenna")
                visible: manageAntennaBtn.hovered
                target: manageAntennaBtn
            }
        }

        RoundButton {
            id: testsBtn
            anchors.horizontalCenter: parent.horizontalCenter
            Layout.fillHeight: false
            implicitHeight: parent.width / 2 + 20
            implicitWidth: parent.width / 2 + 20
            icon.source: "../../resources/icons/TestIcon.svg"
            radius: 4
            onClicked: paper.navigateToPage("../ui/pages/Tests.qml")
            CTooltip {
                text: qsTr("Tests")
                visible: testsBtn.hovered
                target: testsBtn
            }
        }

        RoundButton {
            id: toolsBtn
            anchors.horizontalCenter: parent.horizontalCenter
            implicitHeight: parent.width / 2 + 20
            implicitWidth: parent.width / 2 + 20
            icon.source: "../../resources/icons/tools.svg"
            radius: 4
            onClicked: paper.navigateToPage("../ui/pages/Tools.qml")
            CTooltip {
                text: qsTr("Tools")
                visible: toolsBtn.hovered
                target: toolsBtn
            }
        }

        // 🔹 Spacer to push the last button to the bottom
        Item {
            width: 1
            height: column.height - (manageAntennaBtn.height + testsBtn.height + toolsBtn.height + settingsBtn.height + 10)
        }

        RoundButton {
            id: settingsBtn
            anchors.horizontalCenter: parent.horizontalCenter
            radius: 4
            // color: "transparent"
            implicitHeight: parent.width / 2 + 20
            implicitWidth: parent.width / 2 + 20
            icon.source: "../../resources/icons/tools.svg"
            onClicked: paper.navigateToPage("../ui/pages/Settings.qml")
            CTooltip {
                text: qsTr("Tools")
                visible: toolsBtn.hovered
                target: toolsBtn
            }
        }
    }
}
