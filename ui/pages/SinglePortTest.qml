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
                spacing: 12
                width: parent.width
                RowLayout {
                    Layout.fillWidth: true
                    Label {
                        Layout.preferredWidth: 100
                        text: qsTr("Antenna Model")
                        color: theme.textColor
                    }
                    CComboBox {
                        id: antennaCombo
                        Layout.preferredWidth: 100
                        currentIndex: -1
                        Layout.fillWidth: true
                        model: antennaModel
                        onCurrentTextChanged: antennaManager.loadAntenna(antennaCombo.currentText)
                    }
                }
                RowLayout {
                    Label {
                        Layout.preferredWidth: 100
                        text: qsTr("Description")
                        color: theme.textColor
                    }
                    CTextField {
                        Layout.preferredWidth: 100
                        Layout.fillWidth: true
                    }
                }
                RowLayout {
                    Layout.fillWidth: true
                    visible: antennaCombo.index != -1
                    CheckBox {
                        id: selectAll
                        Layout.preferredWidth: 40
                        onCheckedChanged: selectAllPorts(checked)
                    }
                    Text {
                        Layout.preferredWidth: 80
                        Layout.fillWidth: true
                        text: qsTr("Port")
                        font.pixelSize: 12
                        color: theme.textColorSecondary
                    }
                    Text {
                        Layout.preferredWidth: 80
                        Layout.fillWidth: true
                        font.pixelSize: 12
                        text: qsTr("Frequency min")
                        color: theme.textColorSecondary
                    }
                    Text {
                        Layout.preferredWidth: 80
                        Layout.fillWidth: true
                        font.pixelSize: 12
                        text: qsTr("Frequency max")
                        color: theme.textColorSecondary
                    }
                    Text {
                        Layout.preferredWidth: 80
                        Layout.fillWidth: true
                        font.pixelSize: 12
                        text: qsTr("Tilt min")
                        color: theme.textColorSecondary
                    }
                    Text {
                        Layout.preferredWidth: 80
                        Layout.fillWidth: true
                        font.pixelSize: 12
                        text: qsTr("Tilt max")
                        color: theme.textColorSecondary
                    }
                }
                ScrollView {
                    Layout.fillWidth: true
                    ColumnLayout {
                        width: parent.width
                        Repeater {
                            id: portRepeater
                            Layout.fillWidth: true
                            model: singlePortList
                            delegate: RowLayout {
                                Layout.fillWidth: true
                                Layout.fillHeight: true
                                CheckBox {
                                    id: selectBox
                                    Layout.preferredWidth: 40
                                }
                                Text {
                                    Layout.preferredWidth: 80
                                    text: modelData.port
                                    font.pixelSize: 16
                                    color: theme.textColor
                                    Layout.fillWidth: true
                                }
                                Text {
                                    Layout.preferredWidth: 80
                                    text: modelData.fR.min
                                    font.pixelSize: 16
                                    color: theme.textColor
                                    Layout.fillWidth: true
                                }
                                Text {
                                    Layout.preferredWidth: 80
                                    text: modelData.fR.max
                                    font.pixelSize: 16
                                    color: theme.textColor
                                    Layout.fillWidth: true
                                }
                                Text {
                                    Layout.preferredWidth: 80
                                    text: modelData.tR.min
                                    font.pixelSize: 16
                                    color: theme.textColor
                                    Layout.fillWidth: true
                                }
                                Text {
                                    Layout.preferredWidth: 80
                                    text: modelData.tR.max
                                    font.pixelSize: 16
                                    color: theme.textColor
                                    Layout.fillWidth: true
                                }
                            }
                        }
                    }
                }
            }
            Item {
                RowLayout {
                    CButton {
                        variant: "text"
                        text: qsTr("Back")
                        onClicked: pageContent.mainStack.pop()
                    }
                }
                RowLayout {
                    CButton {
                        text: qsTr("Start")
                        onClicked: pageContent.mainStack.pop()
                    }
                }
            }
        }
    }

    function selectAllPorts(checked) {
        console.log("slecte", checked);
        for (var i = 0; i < portRepeater.count; i++) {
            var rowItem = portRepeater.itemAt(i);
            if(rowItem && rowItem.selectBox){
                console.log("dflsafd")
            rowItem.selectBox.checked = checked;
            }
        }
    }

    Connections {
        target: antennaManager
        function onFileLoaded(filename, data) {
            console.log(JSON.stringify(data));
            singlePortList = data.ports;
        }
    }
}
