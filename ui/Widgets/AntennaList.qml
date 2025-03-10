import QtQuick
import QtQuick.Controls.Material
import QtQuick.Layouts
import "../Delegate"
import "../Components"

ColumnLayout {
    spacing: 10
    Layout.fillWidth: true
    Layout.fillHeight: true

    RowLayout {
        Layout.fillWidth: true
        Label {
            text: qsTr("Antenna's")
            font.pixelSize: 16
            color: theme.textColorSecondary
            font.bold: true
            Layout.alignment: Qt.AlignLeft
            Layout.leftMargin: 12
        }

        Item {
            Layout.fillWidth: true
        }
        RoundButton {
            Layout.alignment: Qt.AlignRight
            text: "\uFF0B"
            CTooltip {
                visible: parent.hovered
                text: qsTr("Add antenna")
            }
            onClicked: pageContent.mainStack.push("../pages/AddAntenna.qml")
        }
    }

    ListView {
        id: listView
        Layout.fillWidth: true
        Layout.fillHeight: true
        clip: true
        currentIndex: 0
        model: antennaModel
        delegate: FileDelegate {}
    }
}
