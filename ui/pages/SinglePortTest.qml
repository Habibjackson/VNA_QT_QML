import QtQuick
import QtQuick.Controls.Material
import QtQuick.Layouts
import "../Components"
import "../Widgets"

Paper {
    id: testsPage
    property var singlePortList: {}
    ColumnLayout {
        spacing: 10
        height: parent.height
        width: parent.width

        TitleBar {
            Layout.fillWidth: true
            color: "#360d2d"
            title: "Single Port Testing"
        }
        Item {
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.margins: 12
            ColumnLayout {
                width: parent.width
                RowLayout {
                    Layout.fillWidth: true
                    Label {
                        text: qsTr("Antenna Model")
                        color: theme.textColor
                    }
                    CComboBox {
                        id: antennaCombo
                        currentIndex: -1
                        Layout.fillWidth: true
                        model: antennaModel
                        onCurrentTextChanged: antennaManager.loadAntenna(antennaCombo.currentText)
                    }
                }
                RowLayout {
                    Label {
                        text: qsTr("Description")
                        color: theme.textColor
                    }
                    CTextField {
                        Layout.fillWidth: true
                    }
                }
                Repeater {
                    model: singlePortList
                    delegate: Text {
                        text: modelData
                        wrapMode: Text.WordWrap
                        font.pointSize: 12
                    }
                }
            }
        }
        CButton {
            text: qsTr("Back")
            onClicked: pageContent.mainStack.pop()
        }
    }

    Connections {
        target: antennaManager
        function onFileLoaded(filename, data) {
            console.log(JSON.stringify(data))
            singlePortList = data
        }
    }
}
