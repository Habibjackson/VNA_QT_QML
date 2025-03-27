import QtQuick
import QtQuick.Controls.Material
import QtQuick.Layouts
import "../Components"
import "../Widgets"

Paper {
    id: testsPage

    property var singlePortList: []
    property var allPorts: []
    property var selectedPorts: []

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
                height: parent.height
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
                        id: description
                        Layout.preferredWidth: 100
                        Layout.fillWidth: true
                    }
                }
                RowLayout {
                    Layout.fillWidth: true
                    visible: antennaCombo.currentIndex != -1
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
                    id: scroller
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    ColumnLayout {
                        width: scroller.width
                        Repeater {
                            id: portRepeater
                            Layout.fillWidth: true
                            model: singlePortList
                            delegate: RowLayout {
                                width: scroller.width
                                CheckBox {
                                    id: selectBox
                                    onCheckedChanged: handleSelectPort(checked, index)
                                    Layout.preferredWidth: 40
                                    checked: selectedPorts.includes(index)
                                }
                                Text {
                                    Layout.preferredWidth: 80
                                    text: modelData["port"]
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
        }
        RowLayout {
            Layout.margins: 8
            Layout.alignment: Qt.AlignRight
            CButton {
                variant: "text"
                text: qsTr("Back")
                onClicked: pageContent.mainStack.pop()
            }
            CButton {
                text: qsTr("Start")
                enabled: selectedPorts.length != 0 || !test.isBusy
                onClicked: startSinglePortTest()
            }
        }
    }

    function selectAllPorts(checked) {
        if (checked) {
            for (var i = 0; i < allPorts.length + 1; i++) {
                handleSelectPort(checked, i);
            }
        }
        if (!checked) {
            selectedPorts = [];
        }
    }

    function startSinglePortTest(){
        var portsSelected = []
        selectedPorts.forEach((ports, i)=>{
            portsSelected.push(singlePortList[ports])
        })
        test.runSinglePort(antennaCombo.currentText.replace(" ", ""), description.text, portsSelected)
    }

    function handleSelectPort(checked, index) {
        var tempList = selectedPorts;
        if (checked) {
            if (!selectedPorts.includes(index)) {
                tempList.push(index);
                selectedPorts = tempList;
            }
        }
        if (!checked) {
            selectedPorts = selectedPorts.filter(item => item !== index);
        }
    }

    Connections {
        target: antennaManager
        function onFileLoaded(filename, data) {
            singlePortList = [];
            allPorts = [];
            var tempList = [];
            console.log(JSON.stringify(data));
            for (var i = 0; i < data.allPorts.length; i++) {
                var port = data.ports[data.allPorts[i]];
                tempList.push({
                    "port": data.allPorts[i],
                    "fR": port.fR,
                    "tR": port.tR,
                    "index": i + 1 // Initialize all items as unselected
                });
            }
            allPorts = data.allPorts;
            singlePortList = tempList;
        }
    }
}
