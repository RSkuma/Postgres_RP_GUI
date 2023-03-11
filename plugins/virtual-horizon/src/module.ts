import { PanelPlugin } from '@grafana/data';
import { SimpleOptions } from './types';
import { SimplePanel } from './components/SimplePanel';

export const plugin = new PanelPlugin<SimpleOptions>(SimplePanel).setPanelOptions((builder) => {
  return builder
    .addTextInput({
      path: 'text',
      name: 'Simple text option',
      description: 'Description of panel option',
      defaultValue: 'Default value of text input option',
    })
    .addBooleanSwitch({
      path: 'showSeriesCount',
      name: 'Show series counter',
      defaultValue: false,
    })
    .addRadio({
      path: 'seriesCountSize',
      defaultValue: 'sm',
      name: 'Series counter size',
      settings: {
        options: [
          {
            value: 'sm',
            label: 'Small',
          },
          {
            value: 'md',
            label: 'Medium',
          },
          {
            value: 'lg',
            label: 'Large',
          },
        ],
      },
      showIf: (config) => config.showSeriesCount,
    }).addRadio({
	      path: 'gap',
	      defaultValue: 5,
	      name: 'Gap in degress between marks',
	      settings: {
		      options: [
			      {
				      label: '5',
				      value: 5,
			      },
			      {
				      label: '10',
				      value: 10,
			      },
			      {
				      label: '15',
				      value: 15,
			      },
			      {
				      label: '20',
				      value: 20,
			      },
		      ]
	      }
      }).addRadio({
	      path: 'gapBetweenEmpMarks',
	      defaultValue : 3,
	      name: 'Gap between emphasized marks',
	      settings: {
		      options: [
			      {
				      label: '1',
				      value: 1,
			      },
			      {
				      label: '2',
				      value: 2,
			      },
			      {
				      label: '3',
				      value: 3,
			      },
			      {
				      label: '4',
				      value: 4,
			      },
		      ]
	      }
      });
});
